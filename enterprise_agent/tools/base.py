"""Normalized research-tool contract (design plan section 10).

Every tool returns a ``ToolResult`` rather than arbitrary prose, so the research
loop never has to parse provider-specific shapes. A successful result with zero
records and a normalized error are different outcomes and must stay different.
"""

from __future__ import annotations

from typing import Any, Protocol

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from enterprise_agent.models.domain import NonBlankStr, SourceUrl


class ToolError(BaseModel):
    """A normalized tool failure, safe to route on."""

    model_config = ConfigDict(extra="forbid")

    code: NonBlankStr
    message: NonBlankStr
    retryable: bool = False


class ToolRecord(BaseModel):
    """One retrieved record with enough provenance to cite it later."""

    model_config = ConfigDict(extra="forbid")

    content: NonBlankStr
    source_url: SourceUrl
    source_title: NonBlankStr
    source_location: NonBlankStr | None = None
    retrieved_at: AwareDatetime


class ToolResult(BaseModel):
    """The single shape every research tool returns."""

    model_config = ConfigDict(extra="forbid")

    tool_name: NonBlankStr
    query_or_input: NonBlankStr
    records: list[ToolRecord] = Field(default_factory=list)
    cost_metadata: dict[str, Any] = Field(default_factory=dict)
    error: ToolError | None = None


class ResearchTool(Protocol):
    """An interchangeable research action."""

    name: str

    async def execute(self, query_or_input: str) -> ToolResult: ...
