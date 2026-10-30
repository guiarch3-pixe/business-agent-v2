"""Persistent company-scoped dense retrieval followed by cross-encoder reranking."""
from __future__ import annotations

import asyncio
import json
import re
import sqlite3
from pathlib import Path
from typing import Protocol
from urllib.parse import urlparse

import numpy as np
from bs4 import BeautifulSoup

from enterprise_agent.schema import Source, Chunk, Hit, digest


class Embedder(Protocol):
    name: str
    def encode(self, texts: list[str], *, text_type="document") -> np.ndarray: ...


class Reranker(Protocol):
    name: str
    def score(self, query: str, documents: list[str]) -> list[float]: ...


class LocalEmbedder:
    def __init__(self, name: str):
        self.name = name
        self._model = None

    def encode(self, texts, *, text_type="document"):
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            self._model = SentenceTransformer(self.name, device="cpu", trust_remote_code=False)
            self._model.max_seq_length = 512
        return self._model.encode(texts, normalize_embeddings=True, show_progress_bar=False)


class LocalReranker:
    def __init__(self, name: str):
        self.name = name
        self._model = None

    def score(self, query, documents):
        if not documents:
            return []
        if self._model is None:
            from sentence_transformers import CrossEncoder
            self._model = CrossEncoder(self.name, device="cpu", max_length=512, trust_remote_code=False)
        return np.asarray(self._model.predict([(query, x) for x in documents],
                                              show_progress_bar=False)).reshape(-1).tolist()


def clean_text(text: str, *, html: bool = False) -> str:
    if html:
        soup = BeautifulSoup(text, "html.parser")
        for tag in soup(["script", "style", "noscript", "nav", "footer", "template"]):
            tag.decompose()
        body = soup.find("main") or soup.find("article") or soup.body or soup
        text = body.get_text(" ", strip=True)
    return " ".join(text.split())


_COMMUNITY_HOSTS = frozenset({"answers.microsoft.com", "techcommunity.microsoft.com",
                              "community.powerplatform.com"})
_VENDOR_HOST_SUFFIXES = (".microsoft.com", ".microsoft365.com", ".azure.com",
                         ".office.com", ".dynamics.com", ".powerplatform.com", ".aka.ms")
_COMMON_SECOND_LEVEL_SUFFIXES = frozenset({
    "co.uk", "org.uk", "com.au", "net.au", "co.nz", "co.jp", "com.br", "com.cn", "co.in",
})


def _company_domain_matches(host: str, company: str | None) -> bool:
    if not company:
        return False
    company_slug = re.sub(r"[^a-z0-9]", "", company.casefold())
    for suffix in (" incorporated", " corporation", " limited", " company", " inc.", " inc",
                   " corp.", " corp", " ltd.", " ltd", " llc", " plc"):
        if company.casefold().endswith(suffix):
            company_slug = re.sub(r"[^a-z0-9]", "", company.casefold()[:-len(suffix)])
            break
    labels = host.split(".")
    if len(labels) < 2:
        return False
    public_suffix = ".".join(labels[-2:])
    registrable_label = labels[-3] if public_suffix in _COMMON_SECOND_LEVEL_SUFFIXES and len(labels) >= 3 else labels[-2]
    domain_slug = re.sub(r"[^a-z0-9]", "", registrable_label)
    if not company_slug or not domain_slug:
        return False
    if domain_slug == company_slug:
        return True
    # Some vendors use a prefixed brand domain (Fathom: usefathom.com). A suffix
    # match is only safe for names long enough not to be a generic English word.
    return len(company_slug) >= 5 and domain_slug.endswith(company_slug)


def classify_authority(url: str, kind: str = "web", company: str | None = None,
                       aliases: tuple[str, ...] = ()) -> str:
    """Classify who published a page, not just which host served it.

    A reply in ``learn.microsoft.com/answers`` is community content on a vendor
    domain; treating the domain as the author is exactly the failure this field
    exists to prevent. Vendor-controlled marketing/docs pages remain official.

    ``aliases`` lets a comparison run recognize both companies' own domains
    without pretending the run is about a single vendor.
    """
    if kind == "demo":
        return "demo"
    if kind == "research_material":
        return "research_material"
    parsed = urlparse(url)
    host = (parsed.hostname or "").casefold().rstrip(".")
    path = parsed.path.casefold()
    # SEC filings are primary regulatory disclosures: authoritative for reported
    # financial facts, but not a vendor marketing/licensing page. Keeping this
    # distinct avoids both mislabelling them as "official vendor" content and
    # discarding them as third-party commentary.
    if host == "sec.gov" or host.endswith(".sec.gov"):
        return "regulator_filing"
    if host in _COMMUNITY_HOSTS:
        return "vendor_community"
    if host == "learn.microsoft.com" and "/answers/" in path:
        return "vendor_community"
    if host in {"microsoft.com", "aka.ms"} or host.endswith(_VENDOR_HOST_SUFFIXES):
        return "vendor_official"
    if any(_company_domain_matches(host, name) for name in (company, *aliases) if name):
        return "vendor_official"
    return "third_party"


def make_source(company: str, url: str, title: str, text: str,
                company_aliases: tuple[str, ...] = (), **metadata) -> Source:
    text = clean_text(text)
    metadata.setdefault("authority", classify_authority(
        url, metadata.get("kind", "web"), company, aliases=company_aliases))
    return Source(id="src_" + digest(company.casefold() + "\n" + url + "\n" + text)[:24],
                  company=company, url=url, title=title, text=text, content_hash=digest(text), **metadata)


def split_source(source: Source, size: int = 600, overlap: int = 90) -> list[Chunk]:
    if not 0 <= overlap < size:
        raise ValueError("chunk overlap must be smaller than chunk size")
    chunks = []
    for start in range(0, len(source.text), size - overlap):
        end = min(start + size, len(source.text))
        # Preserve exact source coordinates, including around whitespace boundaries.
        while start < end and source.text[start].isspace():
            start += 1
        while end > start and source.text[end - 1].isspace():
            end -= 1
        if end > start:
            chunks.append(Chunk(id=f"chk_{source.id[4:]}_{start}", source_id=source.id,
                                start=start, end=end, text=source.text[start:end]))
        if end == len(source.text):
            break
    return chunks


def _vectors(values, count: int) -> np.ndarray:
    raw = np.asarray(values)
    # Numpy would happily coerce True to 1.0 and "1.0" to 1.0. An embedding
    # response must already be numeric; type coercion would hide a bad provider.
    if raw.dtype.kind not in {"i", "u", "f"}:
        raise ValueError("embedding returned non-numeric values")
    values = raw.astype(np.float32, copy=False)
    if values.ndim != 2 or values.shape[0] != count or not values.shape[1] or not np.isfinite(values).all():
        raise ValueError("embedding returned invalid count, shape or non-finite values")
    norms = np.linalg.norm(values.astype(np.float64), axis=1, keepdims=True)
    if (norms == 0).any() or not np.isfinite(norms).all():
        raise ValueError("embedding returned a zero vector")
    normalized = values / norms
    if not np.isfinite(normalized).all():
        raise ValueError("embedding normalization produced non-finite values")
    return normalized.astype(np.float32)


class KnowledgeBase:
    """SQLite snapshots and vectors; exact cosine scan is intended for small corpora.

    The embedding identity is stored in the index: changing it requires a new DB.
    Every connection is scoped to a method, allowing CLI/UI worker use.
    """
    def __init__(self, path: Path, embedder: Embedder, reranker: Reranker):
        self.path, self.embedder, self.reranker = Path(path), embedder, reranker
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            # WAL lets concurrent benchmark runs read while another run indexes a
            # page. Without it a single writer locked the whole database and an
            # otherwise healthy run ended with ``database is locked``.
            db.execute("PRAGMA journal_mode=WAL")
            db.executescript("""
            CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS sources (id TEXT PRIMARY KEY, company TEXT NOT NULL, payload TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS chunks (id TEXT PRIMARY KEY, source_id TEXT NOT NULL,
                payload TEXT NOT NULL, vector TEXT NOT NULL);
            CREATE INDEX IF NOT EXISTS source_company ON sources(company);
            """)
            old = db.execute("SELECT value FROM metadata WHERE key='embedding'").fetchone()
            if old and old[0] != embedder.name:
                raise ValueError("资料库 Embedding 模型不一致，请使用新的 --db 路径重新导入")
            db.execute("INSERT OR IGNORE INTO metadata VALUES ('embedding', ?)", (embedder.name,))
            # Authority classification became company-aware after the first
            # version of this index. Promote matching company domains already
            # stored as third-party so official-only retrieval can see them.
            # Run the migration once: decoding every source on each startup made
            # a large benchmark database slow to open.
            migrated = db.execute(
                "SELECT value FROM metadata WHERE key='authority_scheme'").fetchone()
            if migrated is None:
                for source_id, payload in db.execute("SELECT id, payload FROM sources").fetchall():
                    source = Source.model_validate_json(payload)
                    authority = classify_authority(source.url, source.kind, source.company)
                    if (source.authority in {"third_party", "unknown"}
                            and authority in {"vendor_official", "regulator_filing"}):
                        upgraded = source.model_copy(update={"authority": authority})
                        db.execute("UPDATE sources SET payload=? WHERE id=?",
                                   (upgraded.model_dump_json(), source_id))
                db.execute("INSERT OR REPLACE INTO metadata VALUES ('authority_scheme', '2')")

    def connect(self):
        db = sqlite3.connect(self.path, timeout=60)
        # ``timeout`` covers the initial lock wait; busy_timeout also covers
        # subsequent statements in the same connection.
        db.execute("PRAGMA busy_timeout=60000")
        return db

    def add(self, source: Source) -> int:
        with self.connect() as db:
            if db.execute("SELECT 1 FROM sources WHERE id=?", (source.id,)).fetchone():
                return 0
        chunks = split_source(source)
        vectors = _vectors(self.embedder.encode([x.text for x in chunks]), len(chunks))
        with self.connect() as db:
            dimension = str(vectors.shape[1])
            old = db.execute("SELECT value FROM metadata WHERE key='dimension'").fetchone()
            if old and old[0] != dimension:
                raise ValueError("embedding dimension changed")
            db.execute("INSERT OR IGNORE INTO metadata VALUES ('dimension', ?)", (dimension,))
            db.execute("INSERT OR IGNORE INTO sources VALUES (?, ?, ?)",
                       (source.id, source.company.casefold().strip(), source.model_dump_json()))
            db.executemany("INSERT OR IGNORE INTO chunks VALUES (?, ?, ?, ?)",
                           [(c.id, source.id, c.model_dump_json(), json.dumps(v.tolist()))
                            for c, v in zip(chunks, vectors)])
        return len(chunks)

    def ingest_file(self, company: str, path: Path) -> int:
        path = path.resolve()
        if path.suffix.lower() not in {".txt", ".md", ".html", ".htm"}:
            raise ValueError("支持 UTF-8 .txt/.md/.html 材料；PDF 请先转换为文本")
        if path.stat().st_size > 2_000_000:
            raise ValueError("单份材料上限 2 MB，请分拆后导入")
        source = make_source(company, path.as_uri(), path.name,
                             clean_text(path.read_text(encoding="utf-8"), html=path.suffix.lower() in {".html", ".htm"}),
                             kind="research_material", location="local file, cleaned text")
        return self.add(source)

    def retrieve(self, company: str, query: str, candidates: int = 20, top_k: int = 6,
                 authorities: set[str] | None = None) -> list[Hit]:
        return self.retrieve_many([company], query, candidates=candidates, top_k=top_k,
                                  authorities=authorities)

    def retrieve_many(self, companies: list[str], query: str, candidates: int = 20,
                      top_k: int = 6, authorities: set[str] | None = None,
                      literal_terms: list[str] | None = None,
                      preferred_authorities: set[str] | None = None) -> list[Hit]:
        """Retrieve across company partitions for an explicit comparison run.

        ``literal_terms`` adds an exact-text fallback. Dense retrieval and the
        reranker are good at topics but can miss a single table row such as
        "Sep 21, 2026 ... 375.30"; a date-only question then looks uncovered even
        though the row is in an indexed source. Matching those terms directly
        keeps the evidence available without weakening any quote validation.

        ``preferred_authorities`` widens the candidate pool with chunks from
        preferred sources before reranking. A long third-party guide can outrank
        a terse official pricing page in both dense and rerank scores; without
        this pool the official page is never even considered, and the run
        correctly-lookingly concludes that official evidence is missing.
        """
        if not 1 <= top_k <= candidates:
            raise ValueError("top_k must be within the candidate count")
        partitions = list(dict.fromkeys(name.casefold().strip() for name in companies if name.strip()))
        if not partitions:
            return []
        placeholders = ",".join("?" for _ in partitions)
        with self.connect() as db:
            rows = db.execute(
                f"SELECT c.payload, c.vector, s.payload FROM chunks c JOIN sources s "
                f"ON c.source_id=s.id WHERE s.company IN ({placeholders})", partitions).fetchall()
        if authorities is not None:
            rows = [row for row in rows
                    if Source.model_validate_json(row[2]).authority in authorities]
        if not rows:
            return []
        query_vector = _vectors(self.embedder.encode([query], text_type="query"), 1)[0]
        vectors = _vectors([json.loads(r[1]) for r in rows], len(rows))
        if vectors.shape[1] != len(query_vector):
            raise ValueError("query and corpus embedding dimensions differ")
        scores = vectors @ query_vector
        all_order = np.argsort(-scores, kind="stable")
        indices = list(all_order[:candidates])
        preferred_positions: set[int] = set()
        if preferred_authorities:
            seen = set(indices)
            preferred_rows = [index for index, row in enumerate(rows)
                              if Source.model_validate_json(row[2]).authority in preferred_authorities]
            added = 0
            # First the best official chunks by dense score...
            for index in all_order:
                if added >= min(15, candidates):
                    break
                index = int(index)
                if index in seen or index not in preferred_rows:
                    continue
                indices.append(index)
                seen.add(index)
                added += 1
            # ...then official chunks that share several query terms, even when
            # their dense score is low (terse pricing blocks).
            query_tokens = {token for token in re.findall(r"[a-z0-9$%.,-]{3,}", query.casefold())}
            lexical_added = 0
            for index in preferred_rows:
                if lexical_added >= 15 or index in seen:
                    continue
                text = Chunk.model_validate_json(rows[index][0]).text.casefold()
                if sum(token in text for token in query_tokens) >= 2:
                    indices.append(index)
                    seen.add(index)
                    lexical_added += 1
        specific: list[str] = []
        literal_positions: set[int] = set()
        specific_positions: set[int] = set()
        if literal_terms:
            seen = set(indices)
            terms = [term.casefold() for term in literal_terms if len(term) >= 3]
            months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep",
                      "oct", "nov", "dec", "年", "月")
            # A bare "2026" matches every filing; a full date or a comma-grouped
            # amount is the signal that the exact table row exists. Reserve slots
            # for the specific matches first so generic year matches cannot crowd
            # them out.
            specific = [term for term in terms
                        if any(month in term for month in months)
                        or re.search(r"20\d{2}[-/]\d", term) or "," in term or "%" in term]
            generic = [term for term in terms if term not in specific]
            # Specific matches first: a generic "2026" appears in hundreds of
            # filing chunks and would otherwise consume the whole fallback
            # budget before the exact price-table row is ever considered.
            for index, row in enumerate(rows):
                if len(indices) >= candidates + 20:
                    break
                if index in seen:
                    continue
                text = Chunk.model_validate_json(row[0]).text.casefold()
                if any(term in text for term in specific):
                    literal_positions.add(len(indices))
                    indices.append(index)
                    seen.add(index)
            for index, row in enumerate(rows):
                if len(indices) >= candidates + 40:
                    break
                if index in seen:
                    continue
                text = Chunk.model_validate_json(row[0]).text.casefold()
                if any(term in text for term in generic):
                    literal_positions.add(len(indices))
                    indices.append(index)
                    seen.add(index)
        chunks = [Chunk.model_validate_json(rows[i][0]) for i in indices]
        if preferred_authorities:
            preferred_positions = {
                position for position, index in enumerate(indices)
                if Source.model_validate_json(rows[index][2]).authority in preferred_authorities
            }
        specific_match_count: dict[int, int] = {}
        if specific:
            # Mark matches even when the chunk was already a semantic candidate;
            # otherwise a row that happened to enter through dense retrieval gets
            # no reserved slot and can still be reranked out. A table chunk that
            # contains many dates is a stronger match than a filing mentioning
            # one date in passing, so reserve slots by match count first.
            for position, chunk in enumerate(chunks):
                count = sum(term in chunk.text.casefold() for term in specific)
                if count:
                    specific_positions.add(position)
                    specific_match_count[position] = count
            literal_positions.update(specific_positions)
        reranked = np.asarray(self.reranker.score(query, [x.text for x in chunks]), dtype=float)
        if reranked.shape != (len(chunks),) or not np.isfinite(reranked).all():
            raise ValueError("reranker returned invalid count or scores")
        order = list(np.argsort(-reranked, kind="stable"))
        selected: list[int] = []
        if specific_positions:
            specific_order = sorted(specific_positions,
                                    key=lambda j: (-specific_match_count.get(j, 0),
                                                   -float(reranked[j])))
            selected.extend(specific_order[:2])
        elif literal_positions:
            selected.extend([j for j in order if j in literal_positions][:1])
        if preferred_positions:
            # Rerankers favour long, topical marketing pages over terse pricing
            # blocks. Pick one chunk per official source, ordering sources by how
            # well their URL/title matches the query, so a "/pricing" page is not
            # displaced by a blog or release note from the same vendor.
            query_tokens = {token for token in re.findall(r"[a-z0-9$%.,-]{3,}", query.casefold())}

            def source_text(position: int) -> str:
                source = Source.model_validate_json(rows[indices[position]][2])
                return (source.url + " " + source.title).casefold()

            ranked_preferred = sorted(
                preferred_positions,
                key=lambda j: (-sum(token in source_text(j) for token in query_tokens),
                               -sum(token in chunks[j].text.casefold() for token in query_tokens),
                               -float(reranked[j])))
            used_sources: set[str] = set()
            for j in ranked_preferred:
                if len(selected) >= min(top_k, 2):
                    break
                if j in selected:
                    continue
                source_id = chunks[j].source_id
                if source_id in used_sources:
                    continue
                selected.append(j)
                used_sources.add(source_id)
        for j in order:
            if len(selected) >= top_k:
                break
            if j not in selected:
                selected.append(j)
        return [Hit(chunk=chunks[j], source=Source.model_validate_json(rows[indices[j]][2]),
                    vector_score=float(scores[indices[j]]), rerank_score=float(reranked[j]))
                for j in selected[:top_k]]

    async def aretrieve(self, *args, **kwargs):
        return await asyncio.to_thread(self.retrieve, *args, **kwargs)

    async def aretrieve_many(self, *args, **kwargs):
        return await asyncio.to_thread(self.retrieve_many, *args, **kwargs)

    async def aadd(self, source):
        return await asyncio.to_thread(self.add, source)
