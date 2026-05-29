# Changelog

## v0.1.2 — Agent-native Adoption Layer

This release makes the repository easier for AI coding agents and MCP-compatible agent workflows to understand, use, extend, and call safely.

### Added

- `AGENTS.md` as the operating guide for AI coding agents.
- Agent use case documentation for build, validate, PHI risk, summarization, MCP, and larger workflow patterns.
- MCP client configuration documentation for Claude Desktop, Cursor, OpenAI Agents SDK style usage, and generic local MCP clients.
- Security guidance for agents covering prompt injection, PHI leakage, unsafe tool chaining, external API exfiltration, untrusted local files, and DICOM metadata risks.
- Paste-ready agent prompts for building packets, validating packets, checking PHI risk, and running MCP workflows.
- README section for the Agent-native Dental Context Layer.

### Positioning

- Building the Dental Context Layer for AI Agents.
- Local-first Dental Case Packet Builder.
- MCP-compatible tool layer for structured data transformation.

### Safety

- No diagnosis features.
- No treatment recommendation features.
- No clinical interpretation.
- No patient data upload behavior.
- Outputs remain privacy-first and dentist-review-only.

## v0.1.1 — Local MCP Server + Clinical Validation Dataset

This release introduces a local-first MCP interface and the first Clinical Validation Dataset for AI-ready Dental Case Packets.

### Added

- Local MCP server wrapper for agent workflows.
- MCP tool interface for structured dental data transformation.
- `build_dental_case_packet()` MCP tool.
- `validate_case_packet()` MCP tool.
- `summarize_packet()` MCP tool.
- `list_supported_formats()` MCP tool.
- `check_phi_risk()` MCP tool.
- Clinical Validation Dataset v0.1.
- 20 validation cases covering implant planning, missing teeth, orthodontics, endodontics, wisdom teeth, and full jaw anatomy.
- MCP validation suite with generated build, validation, summary, and PHI risk outputs.
- Additional tests for MCP tools and validation dataset artifacts.

### Improved

- PHI risk checking now avoids false positives from packet system timestamps.
- Validation reporting includes aggregate metrics, unsupported formats, warnings, and schema issues.

### Safety

- No diagnosis features.
- No treatment recommendation features.
- No clinical interpretation.
- Local-first and privacy-first workflows only.
- Outputs remain dentist-review-only.

## v0.1.0 — AI-ready Dental Case Packet Developer Preview

Initial public developer preview for the Dental Case Packet specification and reference CLI.

### Added

- CLI build command: `python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output`.
- CLI validate command: `python -m dental_packet validate --input ./case_packet_output/case_packet.json`.
- Dental Case Packet JSON output: `case_packet.json`.
- Markdown report output: `case_packet.md`.
- File manifest and file index with SHA-256 hashes.
- DICOM metadata extraction for non-sensitive fields.
- PHI-safe metadata handling that logs PHI field presence without exporting raw PHI values.
- Intraoral scan file indexing for STL, PLY, and OBJ files.
- Runnable example input and generated example output.
- Pytest coverage for CLI behavior, schema validation, de-identification, and manifests.
- Ruff validation.
- GitHub Actions CI for ruff, pytest, sample build, and sample validation.

### Safety

- No diagnosis features.
- No treatment recommendation features.
- No clinical accuracy claims.
- Outputs are for dentist review and clinical review workflows only.
