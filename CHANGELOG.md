# Changelog

All notable changes to this project are documented here.

This project follows semantic versioning for the reference implementation and explicit versioning
for the Dental Case Packet specification.

## v0.1.0 - 2026-05-29

Initial developer release.

### Added

- Local CLI for building a Dental Case Packet from `examples/sample_input/`.
- CLI validation command for generated `case_packet.json` files.
- Sample input and sample output for a runnable first developer workflow.
- De-identified output copies for supported text and JSON input files.
- File manifest and file index with SHA-256 hashes.
- Markdown case packet report.
- DICOM metadata extraction with PHI field detection logs.
- Intraoral scan file indexing and best-effort mesh metadata parsing.
- Pydantic schema models and validation tests.
- GitHub Actions CI for ruff, pytest, sample build, and sample validation.

### Safety

- The reference implementation does not diagnose.
- The reference implementation does not recommend treatment.
- AI-facing context says outputs are for clinical review only.
- PHI fields are not exported into `case_packet.json`.
