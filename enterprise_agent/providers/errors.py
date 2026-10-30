"""Stable model-call failure type.

A provider failure must be routable without inspecting a raw HTTP response, and
its message must be safe to write into a trace: no request headers, no
credentials and no provider response body.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - typing only, keeps the provider contract loop-free
    from enterprise_agent.providers.base import TokenUsage


class ModelCallError(RuntimeError):
    """A structured model call that did not produce a usable validated value.

    ``schema_errors`` carries bounded, sanitized descriptions of *where* a response
    failed validation — a field path and a pydantic error type. It never carries the
    offending input, the raw response body, a credential or model reasoning: only the
    location and the kind of mismatch, which is what a diagnostic needs.

    ``usage`` carries token counts when the provider *did* answer and the response
    failed later (JSON or schema validation). Any reported tokens were really spent,
    so a failed call must not be reported as having used none. It stays ``None`` when
    no usable response arrived.
    """

    def __init__(
        self,
        code: str,
        message: str,
        *,
        schema_errors: list[str] | None = None,
        usage: "TokenUsage | None" = None,
    ) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message
        self.schema_errors = list(schema_errors or [])
        self.usage = usage
