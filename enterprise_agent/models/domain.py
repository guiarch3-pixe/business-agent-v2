"""Core domain entities for the V1 research state.

Field names and enum values follow design plan section 6. Scope is plain text for
this milestone; unavailable optional fields stay null. ``source_type`` is a
nonblank string on purpose — no source-type ontology is invented here.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated
from urllib.parse import urlparse

from pydantic import AfterValidator, AwareDatetime, BaseModel, ConfigDict, Field, model_validator

ALLOWED_SOURCE_URL_SCHEMES = frozenset({"http", "https", "file"})


def _nonblank(value: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise ValueError("must not be blank")
    return stripped


def _validated_source_url(value: str) -> str:
    candidate = value.strip()
    if not candidate:
        raise ValueError("source_url must not be blank")
    parsed = urlparse(candidate)
    scheme = parsed.scheme.lower()
    if scheme not in ALLOWED_SOURCE_URL_SCHEMES:
        raise ValueError(
            f"source_url scheme must be one of {sorted(ALLOWED_SOURCE_URL_SCHEMES)}"
        )
    if scheme == "file":
        if not parsed.path:
            raise ValueError("file source_url must include a path")
        return candidate

    if not parsed.netloc:
        raise ValueError("source_url must include a host")
    # A non-empty netloc is not enough: "https://:443/a" has a port but no host,
    # "https://example.invalid:bad/a" has an unparseable port, and a host containing
    # whitespace is not a host at all.
    hostname = parsed.hostname
    if not hostname or any(character.isspace() for character in hostname):
        raise ValueError(f"source_url must include a valid host: {candidate!r}")
    try:
        parsed.port
    except ValueError as error:
        raise ValueError(f"source_url has an invalid port: {candidate!r}") from error
    return candidate


NonBlankStr = Annotated[str, AfterValidator(_nonblank)]
SourceUrl = Annotated[str, AfterValidator(_validated_source_url)]


