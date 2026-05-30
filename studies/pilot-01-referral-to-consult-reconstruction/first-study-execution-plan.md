# First Study Execution Plan

This plan describes how a single researcher can complete a 10-pair proof-of-concept study in 1-2 weeks using synthetic, educational, or public cases.

## Goal

Test whether referral-consult artifact pairs can support disciplined partial reconstruction of clinical cognition.

## Scope

- 10 artifact pairs.
- One clinical domain or closely related set of domains.
- No proprietary records.
- No scraping.
- No live patient-care use.
- No claim of generalizable clinical frequency.

## Week 1: Build and Prepare the Dataset

### Day 1: Select Dataset Strategy

Choose one of two paths:

- synthetic-only proof of concept;
- mixed dataset with synthetic cases plus public educational examples.

Recommended first path: synthetic-only, because it is fastest and lets the researcher test the protocol against known reasoning paths.

### Days 2-3: Create or Identify 10 Pairs

Use `sample-pair-template.md` for each pair.

For synthetic cases, deliberately include varied transformations:

- preservation;
- compression;
- reframing;
- mechanism substitution;
- uncertainty loss;
- new cognition;
- missing cognition.

For public educational cases, create referral-like and consultation-like artifacts by abstracting the case structure without copying long source passages.

### Day 4: Apply Artifact Schema

Extract fields from each pair:

- referral reason;
- suspected diagnosis;
- uncertainty statements;
- requested consultation;
- contextual details;
- timeline;
- final assessment;
- differential diagnosis;
- treatment recommendation;
- rationale;
- follow-up plan.

### Day 5: Pilot the Coding Framework

Code 3 pairs using `coding-framework.md`.

Revise internal notes if categories are confusing, but do not change the formal framework until after all 10 pairs are coded.

## Week 2: Code, Score, and Summarize

### Days 6-7: Code All 10 Pairs

Apply the reconstruction protocol to each pair.

For each pair, produce:

- reconstruction hypothesis;
- preserved cognition;
- transformed cognition;
- missing cognition;
- newly introduced cognition;
- drift characterization;
- confidence note.

### Day 8: Score with Rubric

Score each pair from 0-4 on:

- reasoning preservation;
- uncertainty preservation;
- treatment intent preservation;
- cognitive drift;
- introduced reasoning.

### Day 9: Analyze Patterns

Summarize:

- most common transformation types;
- which fields improved reconstruction;
- which fields were usually missing;
- where reconstruction confidence was weakest;
- whether the method was usable by a single researcher.

### Day 10: Write Feasibility Memo

Write a 2-4 page memo answering:

- Can the method be executed on 10 pairs?
- Which coding categories worked?
- Which categories were ambiguous?
- What kind of dataset should v0.2 use?
- What changes are needed before adding a second coder?

## Expected First Results

The first proof of concept should produce:

- 10 completed pair templates;
- 10 reconstruction hypotheses;
- coded transformation categories;
- rubric scores;
- a short feasibility memo.

## Practical Bottleneck

The main bottleneck is not tooling. It is creating or identifying artifact pairs that are realistic enough to stress-test the method without requiring protected clinical records.
