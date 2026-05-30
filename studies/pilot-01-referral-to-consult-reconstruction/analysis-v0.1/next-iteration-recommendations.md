# Next Iteration Recommendations

## Dataset Design

- Include weaker, shorter, and more ambiguous referral artifacts.
- Add consultation notes with less explicit rationale to test reconstruction failure.
- Include at least two cases where downstream cognition is poorly justified.
- Add cases where new information appears between referral and consultation.
- Separate dental, oral medicine, and general medicine subsets for cleaner domain interpretation.

## Coding Framework

- Clarify the distinction between compression and uncertainty loss.
- Add guidance for partial uncertainty compression.
- Define when operational treatment planning counts as translation.
- Add examples of over-inference and under-inference.
- Add a required evidence note for each code.

## Evaluation Rubric

- Add a reconstruction confidence score or confidence label.
- Consider separate scoring for source cognition recovery versus downstream transformation characterization.
- Provide anchor examples for scores 1, 2, and 3 to reduce ceiling effects.
- Clarify that a high cognitive drift score can mean either low drift or well-explained drift.

## Reconstruction Protocol

- Add an explicit over-inference check before finalizing the reconstruction hypothesis.
- Require coders to list at least one alternative reconstruction when confidence is moderate or low.
- Add a step for identifying whether new downstream information justifies drift.
- Create a short coding worksheet for consistent data capture.

## Future Human Coder Workflow

- Use two independent coders for Dataset v0.2.
- Keep coders blinded to Ground Truth Reasoning Notes until the comparison step.
- Track time per case.
- Record coder disagreements as methodological findings.
- Hold an adjudication meeting after independent coding, but preserve original coder files.

## Dataset v0.2 Readiness

The method is ready for a 25-pair v0.2 feasibility dataset if the next dataset includes less polished cases and at least one second coder.
