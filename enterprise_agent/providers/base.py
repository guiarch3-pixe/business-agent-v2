"""Structured-generation contract.

The agent never wants free prose back from a model; it wants a validated domain
object. ``StructuredLLM`` is the provider-independent shape for that, and no
provider SDK is imported here.
"""

from __future__ import annotations

from typing import Generic, Protocol, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from enterprise_agent.models.domain import NonBlankStr

T = TypeVar("T", bound=BaseModel)


class TokenUsage(BaseModel):
    """Token counts for one model call.

    ``None`` means unknown, not zero: a fixture response has no token accounting
    and must not be reported as having used no tokens.
    """

    model_config = ConfigDict(extra="forbid")

    input_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)


class ModelResponse(BaseModel, Generic[T]):
    """A validated structured output plus which model produced it."""

    model_config = ConfigDict(extra="forbid")

    output: T
    model: NonBlankStr
    usage: TokenUsage


class GenerationOptions(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    max_output_tokens: int = Field(gt=0)


class InputEstimate(BaseModel):
    estimated_tokens: int = Field(ge=0)
    method: str
    input_chars: int = Field(ge=0)


class StructuredLLM(Protocol):
    """Generates a value of ``schema`` for ``prompt``.

    Callers pass the target model class explicitly so that validation happens at
    this boundary rather than in downstream reasoning code.
    """

    def estimate_input(self, prompt: str, schema: type[T]) -> InputEstimate: ...

    async def generate(self, prompt: str, schema: type[T], *, options: GenerationOptions | None = None) -> ModelResponse[T]: ...
