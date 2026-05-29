from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any


class RecordKind(StrEnum):
    DICOM = "dicom"
    MESH = "mesh"
    IMAGE = "image"
    TEXT = "text"
    PDF = "pdf"
    JSON = "json"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class IngestedRecord:
    """Source record discovered before normalization.

    The ingestion layer should collect file identity and provenance only. Clinical interpretation
    belongs outside this layer.
    """

    path: Path
    kind: RecordKind
    role: str
    sha256: str
    size_bytes: int
    metadata: dict[str, Any] = field(default_factory=dict)

