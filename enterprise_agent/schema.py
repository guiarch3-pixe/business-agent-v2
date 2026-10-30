"""Pydantic contracts; references and exact quotations are executable invariants."""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, AwareDatetime, model_validator
from enterprise_agent.models.domain import NonBlankStr, SourceUrl


def now() -> datetime:
    return datetime.now(timezone.utc)


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Acquisition(Model):
    run_id: str
    question_id: str
    question: str
    search_id: str | None = None
    query: str | None = None
    requested_url: str


class Source(Model):
    id: NonBlankStr
    company: NonBlankStr
    url: SourceUrl
    title: NonBlankStr
    kind: Literal["web", "research_material", "demo"]
    # Who authored/published the page, not merely which domain hosts it. A Microsoft
    # Q&A reply on learn.microsoft.com is hosted by the vendor but authored by a
    # community member, so it must never be presented as a formal vendor document.
    # "unknown" keeps states written before this field existed readable.
    authority: Literal["vendor_official", "regulator_filing", "vendor_community",
                       "third_party", "research_material", "demo", "unknown"] = "unknown"
    text: NonBlankStr
    content_hash: NonBlankStr
    retrieved_at: AwareDatetime = Field(default_factory=now)
    location: str = "cleaned text"
    truncated: bool = False
    acquisition: Acquisition | None = None

    @model_validator(mode="after")
    def check_hash(self):
        if self.content_hash != digest(self.text):
            raise ValueError("source content hash mismatch")
        return self


class Chunk(Model):
    id: NonBlankStr
    source_id: NonBlankStr
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    text: NonBlankStr


class Hit(Model):
    chunk: Chunk
    source: Source
    vector_score: float
    rerank_score: float


class Question(Model):
    id: NonBlankStr
    text: NonBlankStr
    parent_gap_id: str | None = None
    round: int = Field(ge=0)


class Evidence(Model):
    id: NonBlankStr
    question_id: NonBlankStr
    source_id: NonBlankStr
    chunk_id: NonBlankStr
    quote: NonBlankStr
    start: int = Field(ge=0)
    end: int = Field(gt=0)


class Citation(Model):
    evidence_id: NonBlankStr
    relation: Literal["supports", "contradicts"]


class Claim(Model):
    id: NonBlankStr
    question_id: NonBlankStr
    kind: Literal["fact", "deduction", "business_judgment", "hypothesis"]
    text: NonBlankStr
    status: Literal["supported", "mixed", "contradicted", "unverified"]
    citations: list[Citation] = Field(default_factory=list)
    rationale: NonBlankStr

    @model_validator(mode="after")
    def support(self):
        relations = {c.relation for c in self.citations}
        if self.kind == "hypothesis" and self.status != "unverified":
            raise ValueError("hypotheses must remain unverified")
        if self.status in {"supported", "mixed"} and "supports" not in relations:
            raise ValueError("supported claim needs supporting evidence")
        if self.status in {"contradicted", "mixed"} and "contradicts" not in relations:
            raise ValueError("contradicted claim needs contradicting evidence")
        if self.status == "supported" and "contradicts" in relations:
            raise ValueError("contradicting evidence requires mixed/contradicted status")
        if self.kind == "fact" and not self.citations:
            raise ValueError("a fact needs evidence; otherwise use an unverified hypothesis")
        return self


class Gap(Model):
    id: NonBlankStr
    question_id: NonBlankStr
    description: NonBlankStr
    # Stable short slug supplied by the model (e.g. "copilot-studio-fair-usage").
    # It lets the code merge rewordings of the same missing evidence even when the
    # prose differs; older states without it remain valid.
    topic: str = ""
    priority: int = Field(default=3, ge=1, le=5)
    #: True means the research cannot answer the original goal without it.
    #: False means a residual unknown worth listing but not worth another round.
    blocking: bool = True
    status: Literal["open", "resolved"] = "open"
    claim_ids: list[str] = Field(default_factory=list)
    resolution_claim_ids: list[str] = Field(default_factory=list)
    resolution_reason: NonBlankStr | None = None


class SearchRecord(Model):
    id: NonBlankStr
    question_id: NonBlankStr
    gap_id: NonBlankStr
    query: NonBlankStr
    urls: list[str] = Field(default_factory=list)
    source_ids: list[str] = Field(default_factory=list)
    error: str | None = None
    created_at: AwareDatetime = Field(default_factory=now)


class ResearchState(Model):
    run_id: NonBlankStr
    company: NonBlankStr
    goal: NonBlankStr
    mode: Literal["live", "demo"] = "live"
    questions: list[Question] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    claims: list[Claim] = Field(default_factory=list)
    gaps: list[Gap] = Field(default_factory=list)
    sources: list[Source] = Field(default_factory=list)
    chunks: list[Chunk] = Field(default_factory=list)
    searches: list[SearchRecord] = Field(default_factory=list)
    rounds: int = 0
    stop_reason: str | None = None
    #: Latest direct answer assembled from validated claims. Older checkpoints
    #: remain readable because both fields have defaults.
    answer: str = ""
    answer_claim_ids: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def references(self):
        collections = [self.questions, self.evidence, self.claims, self.gaps,
                       self.sources, self.chunks, self.searches]
        ids = [x.id for group in collections for x in group]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate IDs")
        questions = {x.id: x for x in self.questions}
        evidence = {x.id: x for x in self.evidence}
        claims = {x.id: x for x in self.claims}
        gaps = {x.id: x for x in self.gaps}
        sources = {x.id: x for x in self.sources}
        chunks = {x.id: x for x in self.chunks}
        searches = {x.id: x for x in self.searches}
        for q in self.questions:
            if q.parent_gap_id is not None and q.parent_gap_id not in gaps:
                raise ValueError("question references unknown gap")
            if q.parent_gap_id is not None:
                origin = gaps[q.parent_gap_id].question_id
                if origin not in questions or questions[origin].round >= q.round:
                    raise ValueError("follow-up question must follow the question that raised its gap")
        for c in self.chunks:
            if c.source_id not in sources or sources[c.source_id].text[c.start:c.end] != c.text:
                raise ValueError("chunk does not match source snapshot")
        for e in self.evidence:
            if e.question_id not in questions or e.source_id not in sources or e.chunk_id not in chunks:
                raise ValueError("dangling evidence reference")
            c = chunks[e.chunk_id]
            if (c.source_id != e.source_id or e.start < c.start or e.end > c.end
                    or sources[e.source_id].text[e.start:e.end] != e.quote):
                raise ValueError("evidence quote does not match original source span")
        for c in self.claims:
            if c.question_id not in questions or any(x.evidence_id not in evidence for x in c.citations):
                raise ValueError("dangling claim reference")
        for g in self.gaps:
            if g.question_id not in questions or any(x not in claims for x in g.claim_ids + g.resolution_claim_ids):
                raise ValueError("dangling gap reference")
            if len(g.resolution_claim_ids) != len(set(g.resolution_claim_ids)):
                raise ValueError("gap resolution claims must be unique")
            if g.status == "resolved":
                if not g.resolution_reason or not g.resolution_claim_ids:
                    raise ValueError("resolved gap requires rationale and supported claims")
                if any(claims[x].status != "supported" or claims[x].kind == "hypothesis"
                       for x in g.resolution_claim_ids):
                    raise ValueError("unverified or conflicted claims cannot resolve a gap")
                if any(questions[claims[x].question_id].parent_gap_id != g.id for x in g.resolution_claim_ids):
                    raise ValueError("resolution claim must answer this gap's follow-up question")
        for s in self.searches:
            if s.question_id not in questions or s.gap_id not in gaps or any(x not in sources for x in s.source_ids):
                raise ValueError("dangling search reference")
            if questions[s.question_id].parent_gap_id != s.gap_id:
                raise ValueError("search is attached to a question raised by another gap")
        for claim_id in self.answer_claim_ids:
            if claim_id not in claims:
                raise ValueError("answer references an unknown claim")
        for s in self.sources:
            a = s.acquisition
            # Acquisitions can be historical: a source reused from an older run keeps
            # that run's ids, which are intentionally not in this state's collections.
            if a is None or a.run_id != self.run_id:
                continue
            if a.question_id not in questions or (a.search_id is not None and a.search_id not in searches):
                raise ValueError("dangling acquisition reference")
            if a.search_id is not None:
                record = searches[a.search_id]
                if record.question_id != a.question_id or s.id not in record.source_ids:
                    raise ValueError("acquisition does not match its search record")
        return self


class Plan(Model):
    gap_id: NonBlankStr
    question: NonBlankStr
    query: NonBlankStr
    rationale: NonBlankStr


class Coverage(Model):
    sufficient: bool
    chunk_ids: list[str]
    rationale: NonBlankStr
    missing: str = ""


class QuoteProposal(Model):
    chunk_id: NonBlankStr
    quote: NonBlankStr


class Extraction(Model):
    quotes: list[QuoteProposal]


class GapProposal(Model):
    description: NonBlankStr
    topic: str = ""
    priority: int = Field(default=3, ge=1, le=5)
    blocking: bool = True
    claim_ids: list[str] = Field(default_factory=list)


class Assessment(Model):
    claims: list[Claim]
    new_gaps: list[GapProposal] = Field(default_factory=list)
    resolve_gap: bool = False
    resolution_claim_ids: list[str] = Field(default_factory=list)
    rationale: NonBlankStr
    #: Short, direct answer to the original goal, assembled only from this round's
    #: validated claims. It is rendered first in the report; the claims remain the
    #: citable source of truth.
    answer: str = ""
    answer_claim_ids: list[str] = Field(default_factory=list)

    @classmethod
    def normalize_payload(cls, data):
        """Repair only status/kind labels that contradict the citations given.

        Model providers call this before strict validation. Evidence, quotes and
        relations are never invented: an unsupported ``fact`` becomes an
        unverified hypothesis, and a ``supported`` label with only contradicting
        citations becomes ``contradicted`` (or ``mixed`` when both exist).
        Saved states are still validated strictly.
        """
        if not isinstance(data, dict) or not isinstance(data.get("claims"), list):
            return data
        for claim in data["claims"]:
            if not isinstance(claim, dict):
                continue
            citations = claim.get("citations") or []
            relations = {c.get("relation") for c in citations if isinstance(c, dict)}
            kind, status = claim.get("kind"), claim.get("status")
            if kind == "hypothesis":
                claim["status"] = "unverified"
            elif kind == "fact" and not citations:
                claim["kind"] = "hypothesis"
                claim["status"] = "unverified"
            elif status == "supported" and "contradicts" in relations:
                claim["status"] = "mixed" if "supports" in relations else "contradicted"
            elif status in {"supported", "mixed", "contradicted"} and not relations:
                claim["status"] = "unverified"
            elif status == "mixed" and "contradicts" not in relations:
                claim["status"] = "supported" if "supports" in relations else "unverified"
            elif status == "contradicted" and "contradicts" not in relations:
                claim["status"] = "unverified"
        return data
