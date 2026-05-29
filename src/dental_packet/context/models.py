from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class DentalContext:
    """Non-diagnostic structured context assembled for dentist review."""

    case_overview: str
    known_information: list[str] = field(default_factory=list)
    missing_information: list[str] = field(default_factory=list)
    clinical_review_questions: list[str] = field(default_factory=list)

