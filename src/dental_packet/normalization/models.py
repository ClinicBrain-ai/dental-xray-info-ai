from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from dental_packet.ingestion import IngestedRecord


@dataclass(frozen=True)
class NormalizedRecord:
    """Canonical metadata for an ingested dental record."""

    source: IngestedRecord
    standard_metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

