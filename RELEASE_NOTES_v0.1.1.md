# v0.1.1 — Local MCP Server + Clinical Validation Dataset

This release introduces a local-first MCP interface and the first Clinical Validation Dataset for AI-ready Dental Case Packets.

`ai-ready-dental-case-packet` remains an AI-native dental data infrastructure project. It is a local-first Dental Context Layer for AI agents, dental teams, and developers who need structured, privacy-first records for clinical review and AI workflows.

This release is not diagnostic, not a medical device, and not a treatment recommendation system. Outputs are dentist-review-only.

## What’s New

- Local MCP server wrapper for AI agent workflows.
- MCP-compatible tool interface for Dental Case Packet operations.
- Clinical Validation Dataset v0.1 with 20 infrastructure validation cases.
- MCP validation suite with stored build, validation, summary, and PHI risk outputs.
- PHI risk improvements to reduce false positives from packet system fields.
- Additional pytest coverage for MCP tools and validation artifacts.

## Local MCP Server

The MCP server lets compatible AI agents use this repository as a local tool layer without sending patient data to external APIs.

Exposed tools:

- `build_dental_case_packet()`
- `validate_case_packet()`
- `summarize_packet()`
- `list_supported_formats()`
- `check_phi_risk()`

Install:

```bash
pip install -e ".[mcp]"
```

Run:

```bash
python -m dental_packet_mcp
```

## Clinical Validation Dataset v0.1

The validation dataset is built from public-source-referenced, anonymized local fixtures only. It does not contain private patient data and does not perform imaging interpretation.

Representative coverage includes:

- Implant planning
- Missing teeth
- Orthodontics
- Endodontics
- Wisdom teeth
- Full jaw anatomy

## Validation Metrics

- 20 validation cases
- 20/20 packet builds successful
- 20/20 MCP executions successful
- 20/20 packet validations successful
- PHI risk: low=20, medium=0, high=0
- Unsupported formats observed: `.gz`, `.pdf`
- `pytest`: 15 passed
- `ruff check .`: passed

## Known Limitations

- The validation dataset uses lightweight local fixtures and public dataset references rather than bundling large third-party imaging datasets.
- PDF and NIfTI-style source exports are indexed but not parsed.
- DICOM support remains metadata-focused.
- `summarize_packet()` returns non-diagnostic packet context only.
- `check_phi_risk()` detects obvious PHI-like fields and patterns but is not a substitute for formal privacy review.
- No LLM API calls are included.

## Roadmap

- Batch MCP validation tool.
- Structured warning taxonomy.
- JSON Schema validation in the MCP validator.
- Dedicated provenance fields in the Dental Case Packet schema.
- Better unsupported-format reporting.
- Optional local DICOM thumbnail service.
- FHIR interoperability mapping.

## Safety Disclaimer

Dental Case Packets are structured context artifacts for review workflows. They are not medical advice, diagnosis, treatment planning, clinical decision support, or treatment recommendations. All generated outputs must be reviewed by qualified dental professionals before any clinical use.
