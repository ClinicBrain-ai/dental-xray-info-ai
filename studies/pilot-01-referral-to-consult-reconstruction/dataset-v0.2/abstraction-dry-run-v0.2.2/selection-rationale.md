# Selection Rationale

Dataset v0.2.2 selects only two candidates from the v0.2.1 abstraction batch. This dry run is intended to test abstraction safety and workflow usability before expanding to the remaining candidates.

No source text has been copied. This file records source-selection rationale only.

| Candidate ID | Specialty | Reason selected | Main expected transformation type | Privacy risk | Copyright risk | Methodological value | Why suitable for dry run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAND-006 | Endodontics / periodontics | Clear referral-like uncertainty between endodontic and periodontal mechanisms with a downstream sequential specialist plan. | mechanism substitution | medium | medium | high | It provides a strong dental-domain cognitive transition without rare-disease identifiability and can be abstracted at high level without images or exact chronology. |
| CAND-012 | Cardiology | Clear initial uncertainty around chest-pain evaluation and downstream specialist reasoning. | compression | medium | medium | high | It tests whether the template can handle a general medicine case while preserving uncertainty and avoiding clinical-guidance tone. |

## Dry-Run Boundary

Only these two candidates are abstracted in v0.2.2. The remaining eight v0.2.1 candidates should wait until these abstractions receive human review.
