# v0.1.2 — Agent-native Adoption Layer

`ai-ready-dental-case-packet` is building the Dental Context Layer for AI Agents.

This release makes the repository easier for Codex, Cursor, Claude Code, OpenAI Agents, Claude Desktop, and other agent workflows to understand, use, extend, and call safely.

The project remains local-first, privacy-first, and dentist-review-only. It is not a diagnostic system, not a treatment recommendation system, not a medical device, and not a cloud upload service.

## What's New

### AGENTS.md

Added `AGENTS.md` as the operating guide for AI coding agents.

It explains:

- project mission
- architecture overview
- setup commands
- test commands
- CLI commands
- MCP server commands
- safety boundaries
- prohibited behaviors
- contribution expectations
- where to find specs, docs, examples, and validation reports

### Agent Use Cases

Added `docs/agent-use-cases.md` with safe local workflows for:

- building a Dental Case Packet from a local folder
- validating a packet
- checking PHI risk
- summarizing available and missing records
- using MCP tools from an AI agent
- using this repo as a dental context layer in a larger agent workflow

### MCP Client Config Docs

Added `docs/mcp-client-config.md` with example configurations for:

- Claude Desktop
- Cursor
- OpenAI Agents SDK style usage
- generic local MCP clients

Supported local commands include:

```bash
dental-packet-mcp
python -m dental_packet_mcp
```

### Security Guidance For Agents

Added `docs/security-for-agents.md` covering agent-specific risks:

- prompt injection
- malicious local files
- PHI leakage
- unsafe tool chaining
- external API exfiltration
- untrusted DICOM metadata
- generated summaries being mistaken for diagnosis

The guidance emphasizes local-first execution, no external API calls by default, no raw PHI printing, no automatic upload, and dentist-review-only outputs.

### Paste-ready Agent Prompts

Added prompt examples under `examples/agent_prompts/`:

- `build_packet.md`
- `validate_packet.md`
- `check_phi.md`
- `mcp_workflow.md`

These prompts are designed to be pasted into an AI agent while preserving the project's safety boundaries.

### README Agent-native Section

Updated the README with an “Agent-native Dental Context Layer” section near the top, linking to the new agent guidance, use cases, MCP client configuration, and security docs.

## How To Try It

```bash
git clone https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet.git
cd ai-ready-dental-case-packet

python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,mcp]"

python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
python -m dental_packet_mcp
```

## Safety Boundaries

- Do not diagnose.
- Do not recommend treatment.
- Do not interpret imaging clinically.
- Do not claim clinical accuracy.
- Do not upload patient data.
- Do not send case data to external APIs.
- Do not print raw PHI values.
- Treat all outputs as for clinical review only.

## Known Limitations

- MCP support is local-first and intentionally minimal.
- Agent prompts are examples, not a guarantee of safe downstream agent behavior.
- PHI risk checks are heuristic and do not replace privacy review.
- The packet schema remains early and may evolve in future versions.
- No clinical validation, diagnosis, or treatment recommendation claims are made.

## Roadmap

- Stronger local MCP server behavior.
- OpenAI Agents SDK example.
- Claude Desktop example.
- Cursor and Codex coding-agent workflow documentation.
- Dental Context Evaluation Harness.
- Schema version negotiation.
- Dental Context Protocol for AI Agents.
