# RFC 0003: FHIR Interoperability Design

Status: Draft  
Created: 2026-05-29

## Summary

Design future Dental Case Packet interoperability with FHIR without turning generated AI context into clinical truth.

## Motivation

Dental systems need exchange formats that can work with broader healthcare infrastructure. FHIR is the likely bridge, but dentistry has gaps around intraoral scans, tooth notation, and AI-ready context.

## Proposal

Map packet concepts to FHIR resources where appropriate:

- DICOM studies to `ImagingStudy`
- source documents to `DocumentReference`
- packet provenance to `Provenance`
- review workflows to `Task`
- photos to `Media` or `DocumentReference`

## Safety Boundary

Generated packet summaries and LLM context must not be exported as diagnoses or treatment recommendations.

