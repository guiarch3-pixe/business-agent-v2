"""Alibaba Cloud native HTTP APIs, with strict response-to-input index mapping."""
from __future__ import annotations

import math
import time
from urllib.parse import urlparse

import httpx
import numpy as np


class RetrievalAPIError(RuntimeError):
    def __init__(self, code):
        self.code = code
        super().__init__(code)  # Never echo a response body, URL query or credential.


class DashScopeClient:
    def __init__(self, api_key, endpoint, model, *, client=None, timeout=40.0):
        if not api_key.strip():
            raise ValueError("请在 V2/.env 填写 DASHSCOPE_API_KEY")
        parsed = urlparse(endpoint)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.query:
            raise ValueError("阿里云 API 地址必须是无凭据、无查询参数的 HTTPS 地址")
        self._api_key, self.endpoint, self.model = api_key, endpoint, model
        self.client, self.timeout = client, timeout
        self.deadline = None
        self.before_request = None
        self.on_result = None
        self.cancelled = False

    def post(self, payload, kind):
        if self.cancelled or (self.deadline is not None and time.monotonic() >= self.deadline):
            raise RetrievalAPIError("retrieval_cancelled_or_timed_out")
        timeout = min(self.timeout, max(0.1, self.deadline - time.monotonic())) if self.deadline else self.timeout
        response = None
        for attempt in range(3):
            if self.before_request:
                self.before_request(kind)
            try:
                if self.client is None:
                    with httpx.Client(timeout=timeout) as client:
                        response = client.post(self.endpoint,
                                               headers={"Authorization": f"Bearer {self._api_key}"},
                                               json=payload, timeout=timeout, follow_redirects=False)
                else:
                    response = self.client.post(self.endpoint,
                                                headers={"Authorization": f"Bearer {self._api_key}"},
                                                json=payload, timeout=timeout, follow_redirects=False)
            except httpx.HTTPError as exc:
                if attempt < 2:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                raise RetrievalAPIError("retrieval_network_error") from exc
            if response.status_code in {429, 500, 502, 503, 504} and attempt < 2:
                time.sleep(1.5 * (attempt + 1))
                continue
            break
        if response is None:
            raise RetrievalAPIError("retrieval_network_error")
        if response.status_code != 200:
            raise RetrievalAPIError(f"retrieval_http_{response.status_code}")
        try:
            data = response.json()
        except ValueError as exc:
            raise RetrievalAPIError("retrieval_invalid_json") from exc
        if not isinstance(data, dict) or data.get("code") or not isinstance(data.get("output"), dict):
            raise RetrievalAPIError("retrieval_invalid_response")
        tokens = data.get("usage", {}).get("total_tokens") if isinstance(data.get("usage"), dict) else None
        if not isinstance(tokens, int) or isinstance(tokens, bool) or tokens < 0:
            tokens = None
        if self.on_result:
            self.on_result(kind, self.model, tokens)
        return data["output"]


def indexed(rows, count, index_name):
    if not isinstance(rows, list) or len(rows) != count:
        raise RetrievalAPIError("retrieval_result_count_mismatch")
    mapped = {}
    for row in rows:
        index = row.get(index_name) if isinstance(row, dict) else None
        if type(index) is not int or not 0 <= index < count or index in mapped:
            raise RetrievalAPIError("retrieval_invalid_indices")
        mapped[index] = row
    return [mapped[i] for i in range(count)]


class DashScopeEmbedder(DashScopeClient):
    def __init__(self, api_key, endpoint, model="text-embedding-v4", *, dimensions=1024, **kwargs):
        super().__init__(api_key, endpoint, model, **kwargs)
        if dimensions not in {64, 128, 256, 512, 768, 1024, 1536, 2048}:
            raise ValueError("不支持的 text-embedding-v4 向量维度")
        self.dimensions = dimensions
        self.name = f"dashscope:{model}:{dimensions}:query-document-v1"

    def encode(self, texts, *, text_type="document"):
        if text_type not in {"query", "document"}:
            raise ValueError("invalid text_type")
        vectors = []
        # text-embedding-v4 accepts at most 10 texts per request.
        for start in range(0, len(texts), 10):
            batch = texts[start:start + 10]
            output = self.post({"model": self.model, "input": {"texts": batch},
                                "parameters": {"dimension": self.dimensions, "text_type": text_type,
                                               "output_type": "dense"}}, "embedding_calls")
            rows = indexed(output.get("embeddings"), len(batch), "text_index")
            dense = []
            for row in rows:
                vector = row.get("embedding")
                # Reject bools and strings explicitly: numpy would silently coerce
                # them to 1.0 / 1.0, hiding a malformed provider response.
                if not isinstance(vector, list) or len(vector) != self.dimensions or any(
                        isinstance(value, bool) or not isinstance(value, (int, float))
                        for value in vector):
                    raise RetrievalAPIError("embedding_invalid_vectors")
                dense.append(vector)
            try:
                values = np.asarray(dense, dtype=np.float32)
            except (ValueError, TypeError, OverflowError) as exc:
                raise RetrievalAPIError("embedding_invalid_vectors") from exc
            if values.shape != (len(batch), self.dimensions) or not np.isfinite(values).all():
                raise RetrievalAPIError("embedding_invalid_vectors")
            vectors.extend(values.tolist())
        return np.asarray(vectors, dtype=np.float32).reshape(len(texts), self.dimensions)


class DashScopeReranker(DashScopeClient):
    def __init__(self, api_key, endpoint, model="qwen3-rerank", **kwargs):
        super().__init__(api_key, endpoint, model, **kwargs)
        self.name = "dashscope:" + model

    def score(self, query, documents):
        if not documents:
            return []
        output = self.post({"model": self.model, "input": {"query": query, "documents": documents},
                            "parameters": {"top_n": len(documents), "return_documents": False}}, "reranker_calls")
        rows = indexed(output.get("results"), len(documents), "index")
        scores = []
        for row in rows:
            value = row.get("relevance_score")
            if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
                raise RetrievalAPIError("reranker_invalid_scores")
            scores.append(float(value))
        return scores
