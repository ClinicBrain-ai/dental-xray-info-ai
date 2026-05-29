# Compatibility Strategy

Status: Draft

## Compatibility Goals

The Dental Case Packet should be stable enough for:

- LLM connectors
- clinical review tools
- data pipelines
- future dental agents
- downstream validation systems

## Consumer Compatibility

Consumers SHOULD:

- ignore unknown optional fields in non-strict mode
- preserve unknown extension fields when round-tripping
- fail closed on safety flags
- treat absent data as unknown, not negative
- avoid interpreting missing imaging as clinical meaning

## Producer Compatibility

Producers SHOULD:

- emit the oldest version they can support when requested
- include schema metadata when available
- avoid moving fields without a major version
- include provenance for generated fields
- include manifest hashes for referenced artifacts

## Extension Strategy

Future versions SHOULD reserve:

```json
{
  "extensions": {
    "org.example.feature": {}
  }
}
```

Extension authors SHOULD document:

- namespace
- owner
- schema
- privacy behavior
- safety behavior
- compatibility guarantees

## Breaking Change Policy

Before v1.0, breaking changes are allowed but should be documented in RFCs.

After v1.0:

- breaking changes require a MAJOR version
- migration notes are required
- compatibility fixtures are required
- validators should support at least one previous minor version

## Safety Compatibility

Safety flags are fail-closed. If a consumer does not understand safety semantics, it MUST NOT present the packet as clinically actionable.

