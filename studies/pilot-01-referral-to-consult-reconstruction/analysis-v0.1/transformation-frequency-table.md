# Transformation Frequency Table

Dataset v0.1 is synthetic and educational. Counts reflect this designed proof-of-concept set, not clinical prevalence.

| Transformation type | Count | Brief interpretation |
| --- | ---: | --- |
| Preservation | 10 | Every case preserved the central referral concern in the consultation note. This is partly by dataset design. |
| Compression | 7 | Specialist notes often converted uncertainty into a more actionable assessment or plan. |
| Delegation | 10 | Each referral delegated interpretation, decision-making, or treatment planning to a specialist. |
| Translation | 3 | Several consults converted referral uncertainty into operational testing, biopsy, or follow-up pathways. |
| Reframing | 6 | The downstream specialist often changed the organizing diagnostic or management frame. |
| Diagnostic Replacement | 3 | Three cases shifted from an initial suspected diagnosis toward a different leading diagnosis. |
| Mechanism Substitution | 5 | Several cases changed the causal explanation for the same symptom or finding. |
| Uncertainty Loss | 0 | The coding pass did not assign strict uncertainty loss because specialist notes usually preserved some uncertainty. Compression was more common than full loss. |
| New Cognition | 10 | Every specialist note introduced additional differential, rationale, workup, or treatment structure. |
| Missing Cognition | 10 | Every case had some missing upstream detail that limited reconstruction precision. |

## Interpretation

The most common transformation patterns were preservation, delegation, new cognition, and missing cognition. This means the workflow can detect both continuity and incompleteness, but Dataset v0.1 may be too clean: the referral letters were intentionally informative, and the consultation notes usually explained their drift.
