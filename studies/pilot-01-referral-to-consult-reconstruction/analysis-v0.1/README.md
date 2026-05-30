# Analysis v0.1

This directory contains the first proof-of-concept coding pass for Dataset v0.1 of the referral-to-consult reconstruction pilot.

Dataset v0.1 is synthetic and educational. The analysis tests whether the reconstruction workflow can produce interpretable outputs; it does not claim real-world validity or estimate real clinical frequencies.

## Method

The initial case-coding files were created using only the Referral Letter and Specialist Consultation Note from each synthetic case. Ground Truth Reasoning Notes were excluded from the initial reconstruction pass and used only later in `ground-truth-comparison.md`.

Coding used:

- `../coding-framework.md`
- `../evaluation-rubric.md`
- `../reconstruction-protocol.md`

## Contents

- `case-coding/`: one coding file per synthetic case.
- `results-table.md`: aggregate rubric scores and confidence judgments.
- `transformation-frequency-table.md`: transformation category counts.
- `ground-truth-comparison.md`: post-hoc comparison against hidden ground truth notes.
- `feasibility-memo.md`: feasibility conclusions.
- `next-iteration-recommendations.md`: recommended changes for Dataset v0.2.
