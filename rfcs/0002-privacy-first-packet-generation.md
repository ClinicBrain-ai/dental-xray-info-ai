# RFC 0002: Privacy-first Packet Generation

Status: Accepted  
Created: 2026-05-29

## Summary

Dental Case Packet producers must de-identify by default and use allowlists for exported clinical metadata.

## Motivation

Dental records can contain PHI in structured fields, free text, filenames, image pixels, DICOM private tags, PDFs, and photographs. A packet standard must fail toward privacy.

## Decision

- Use allowlists for DICOM metadata export.
- Treat raw PHI values as forbidden in packet JSON.
- Log PHI field names only when needed.
- Require `patient.deidentified = true`.
- Require safety flags in every packet.

## Consequences

The spec may omit potentially useful metadata if privacy risk is unclear. Future versions can add explicit privacy profiles and review workflows.

