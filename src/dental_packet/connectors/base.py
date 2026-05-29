from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LlmConnectorRequest:
    """Provider-neutral request envelope for future LLM connectors."""

    provider: str
    prompt_context: str
    model: str | None = None
    for_clinical_review_only: bool = True
    allow_diagnosis: bool = False
    allow_treatment_recommendations: bool = False

    def validate_safety(self) -> None:
        if not self.for_clinical_review_only:
            raise ValueError("LLM connector requests must be for clinical review only.")
        if self.allow_diagnosis:
            raise ValueError("LLM connector requests must not allow diagnosis.")
        if self.allow_treatment_recommendations:
            raise ValueError("LLM connector requests must not allow treatment recommendations.")

