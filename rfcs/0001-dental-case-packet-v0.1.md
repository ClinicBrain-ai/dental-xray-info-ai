# RFC 0001: Dental Case Packet v0.1

Status: Accepted  
Created: 2026-05-29

## Summary

Define the initial Dental Case Packet as a de-identified JSON context object for AI-ready dental records.

## Motivation

Dental data is fragmented across imaging systems, notes, treatment plans, scans, and photos. LLM and agent workflows need a predictable context layer that is not a diagnostic system and does not embed large source artifacts.

## Decision

Adopt a v0.1 JSON packet with:

- case identity
- de-identified patient demographics
- narrative summaries
- imaging inventory
- AI-ready context
- safety flags

## Consequences

The first version is intentionally small. It enables reference implementation work while leaving room for provenance, extension fields, FHIR mappings, and richer normalized records.

