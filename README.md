# Clinical Cognition Transformation Lab (CCTL)

Studying the transformation of clinical cognition in distributed human-AI healthcare systems.

## Start Here

For new readers, [Status Report v1.0](docs/status-report-v1.0.md) is the best entry point for understanding the current repository status, completed work, active boundaries, and closed Dataset v0.2 cycle.

- [Status Report v1.0](docs/status-report-v1.0.md)
- [Manifesto](docs/manifesto.md)
- [Research Note 001](research-notes/001-synthetic-referral-consult-reconstruction-feasibility.md)

This repository is research-oriented and educational; it does not provide clinical guidance, diagnosis, treatment recommendations, or patient-care advice.

## Why This Lab Exists

Healthcare is entering a period in which clinical judgment is no longer produced only inside the mind of an individual clinician. Decisions increasingly emerge through interactions among clinicians, AI systems, documentation artifacts, institutional workflows, healthcare organizations, patients, and caregivers.

CCTL exists to study this transformation as a scientific object in its own right.

The lab originated in dental AI infrastructure work, including the AI-ready Dental Case Packet and the Dental Context Specification (DCS). Those projects remain important origins and downstream artifacts, but they are no longer the organizing center of this repository.

## Latest Research Output

CCTL has completed a first synthetic feasibility study: [Research Note 001: Synthetic Referral-to-Consult Reconstruction Feasibility Study](research-notes/001-synthetic-referral-consult-reconstruction-feasibility.md). Dataset v0.1 contains 10 fictional educational referral-consult pairs, and the first coding pass tested whether the reconstruction workflow produces interpretable outputs.

Dataset v0.1 uses fictional educational cases only. It is not clinical guidance, not patient-care advice, and not evidence of real-world clinical frequency or validity.

## Core Thesis

Clinical cognition is no longer exclusively an individual cognitive activity. It is increasingly a distributed process emerging from interactions among clinicians, AI systems, documentation artifacts, institutions, and patients.

The scientific challenge is no longer understanding clinical reasoning alone. The scientific challenge is understanding how clinical cognition transforms within distributed human-AI systems.

## Human-AI Clinical Cognition

Human-AI Clinical Cognition refers to the distributed cognitive processes that emerge when clinical decisions are jointly produced by clinicians, AI systems, documentation artifacts, institutional workflows, healthcare organizations, patients, and caregivers.

This framing treats AI not merely as a tool that assists a clinician, but as one participant in a broader cognitive system. Clinical cognition may be preserved, compressed, delegated, translated, simplified, reframed, reconstructed, redistributed, reassigned, or transformed as it moves through that system.

## Research Agenda

CCTL studies how clinical cognition changes as healthcare becomes a distributed human-AI cognitive system.

The central questions are:

- How does cognition change as it moves between clinicians, AI systems, documents, workflows, organizations, patients, and caregivers?
- What parts of clinical reasoning survive downstream documentation?
- What forms of cognition are delegated to AI systems?
- What forms of expertise are amplified, weakened, displaced, or newly created?
- How can cognitive pathways be represented, traced, audited, and reconstructed?

## Research Programs

1. Clinical Cognition Transformation  
   Study how diagnostic framing, uncertainty, recommendations, mechanisms, and responsibilities change across healthcare systems.

2. Cognitive Reconstruction  
   Study whether prior cognition can be reconstructed from downstream artifacts such as referral letters, consultation notes, treatment plans, clinical documentation, and longitudinal records.

3. Human-AI Co-Cognition  
   Study hybrid cognitive systems in which humans and AI jointly produce clinical interpretation, recommendation, explanation, or action.

4. Cognitive Provenance  
   Study how cognitive pathways can be represented, traced, audited, compared, and understood.

5. Longitudinal Cognitive Change  
   Study how clinician cognition evolves as AI becomes embedded into daily practice.

## Repository Map

- [Manifesto](docs/manifesto.md)
- [Research Agenda](docs/research-agenda.md)
- [Research Programs](docs/research-programs.md)
- [Papers](papers/)
- [Pilot Studies](studies/)
- [Methods](methods/)
- [Research Notes](research-notes/)
- [Pilot 1: Referral-to-Consult Reconstruction](studies/pilot-01-referral-to-consult-reconstruction/)
- [Pilot 1 Dataset v0.1](studies/pilot-01-referral-to-consult-reconstruction/dataset-v0.1/)
- [Pilot 1 Analysis v0.1](studies/pilot-01-referral-to-consult-reconstruction/analysis-v0.1/)
- [Project Evolution](docs/project-evolution.md)
- [Role of DCS](docs/dcs-role.md)
- [Roadmap](docs/roadmap.md)
- [Founding Statement](docs/founding-statement.md)

## Status Report

For a consolidated overview of the current repository status, completed work, open questions, and current research boundaries, see [Status Report v1.0](docs/status-report-v1.0.md).

## Project Evolution

This repository evolved through a sequence of increasingly broad research framings:

AI-ready Dental Case Packet  
-> Dental Context Specification (DCS)  
-> Reasoning Decay  
-> Clinical Reasoning Reconstruction  
-> Human-AI Co-Reasoning  
-> Clinical Reasoning Transformation  
-> Clinical Cognition Transformation

The dental packet and dental imaging work were early domain-specific infrastructure experiments. They helped reveal a broader problem: the important question was not only how to package dental data for AI, but how clinical cognition changes when intelligence becomes distributed across people, machines, documents, institutions, and patients.

## Role of DCS

DCS is no longer the central project.

DCS is now best understood as a possible cognitive provenance representation layer. It may help encode clinical context, reasoning traces, transformations, uncertainty, and workflow transitions. It remains valuable as a downstream representation experiment, especially because this repository contains historical specification work, schemas, examples, and validation-oriented research materials.

The primary research question is broader than DCS.

## Current Repository Status

This repository is being reframed from a dental AI infrastructure and DCS-centered project into the Clinical Cognition Transformation Lab.

Existing DCS, dental reasoning, case reconstruction, and synthetic workflow materials are preserved as origins and research artifacts. They should be read as historical substrate and experimental infrastructure for studying Human-AI Clinical Cognition, not as the sole mission of the repository.

Package names, schema names, and paths that still contain DCS or dental terminology are retained where changing them would obscure history or break existing materials.

## Future Directions

CCTL will develop studies, methods, and representations for:

- distributed human-AI clinical cognitive systems;
- cognitive provenance;
- cognitive reconstruction from clinical artifacts;
- longitudinal change in clinician expertise;
- human-AI co-cognition in real workflows;
- future clinical expertise in AI-embedded healthcare.

## Founding Statement

Clinical cognition is no longer exclusively an individual cognitive activity.

It is increasingly a distributed process emerging from interactions among clinicians, AI systems, documentation artifacts, institutions, and patients.

The scientific challenge is no longer understanding clinical reasoning alone.

The scientific challenge is understanding how clinical cognition transforms within distributed human-AI systems.

CCTL exists to study that transformation.
