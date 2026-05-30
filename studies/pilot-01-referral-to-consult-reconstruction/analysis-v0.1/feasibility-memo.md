# Feasibility Memo

## Can the Reconstruction Protocol Be Applied to Synthetic Cases?

Yes. The protocol produced interpretable outputs for all 10 synthetic referral-consult pairs. Each case supported a reconstruction hypothesis, transformation codes, rubric scores, and later comparison against hidden ground truth notes.

This result should be interpreted narrowly. Dataset v0.1 was designed to be readable and educational. It does not demonstrate that the method will work equally well on messy real-world records.

## Easiest Coding Categories

The easiest categories were:

- Preservation: central referral concerns were usually easy to trace.
- Delegation: each referral clearly transferred some cognitive work to a specialist.
- New Cognition: specialist notes consistently added differential diagnoses, rationale, or management structure.
- Missing Cognition: even strong referrals omitted some details needed for full reconstruction.

## Ambiguous Coding Categories

The most ambiguous distinction was compression versus uncertainty loss. In most cases, the consultation note narrowed uncertainty but did not erase it. The framework may need clearer guidance for partial uncertainty compression.

Translation was also somewhat ambiguous. Some specialist plans operationalized cognition for action, but not all such operationalization felt like translation in the current definition.

## Did the Rubric Produce Useful Distinctions?

Yes, but with ceiling effects. Most scores were high because the synthetic cases were intentionally structured and the consult notes explained their reasoning. The rubric distinguished moderate cases, especially cases 003, 004, and 006, where causal reasoning and upstream evidence were less fully recoverable.

## What Needs to Change Before Dataset v0.2?

- Add messier referral letters with fewer explicit uncertainty statements.
- Add cases where consultation notes preserve conclusions but omit rationale.
- Clarify compression versus uncertainty loss.
- Add optional scoring for reconstruction confidence.
- Add a structured place to record over-inference.
- Introduce a second coder to test whether categories are reproducible.

## Is This Method Ready to Test on Published Educational Cases?

Yes, cautiously. The method appears feasible enough for Dataset v0.2 using published educational cases, provided the next iteration treats public cases as artifact-like teaching materials rather than authentic workflow records.

The next test should examine whether the protocol still produces useful outputs when referral and consultation artifacts are less cleanly separated.
