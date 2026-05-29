# Versioning Strategy

Status: Draft

## Version Format

The Dental Case Packet Specification uses semantic versioning:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
0.1.0
```

Spec documents may use shortened labels such as `v0.1` when PATCH is not relevant.

## Version Meaning

### MAJOR

Increment MAJOR when a change breaks conforming consumers.

Examples:

- remove a required field
- rename a required field
- change a field type incompatibly
- change safety semantics

### MINOR

Increment MINOR when adding backward-compatible functionality.

Examples:

- add optional fields
- add optional artifact reference types
- add new warning codes
- add new supported source formats
- add a new FHIR mapping table

### PATCH

Increment PATCH for clarifications that do not change packet shape.

Examples:

- editorial fixes
- examples
- non-normative guidance
- validator wording improvements

## Version Fields

Future packets SHOULD include:

```json
{
  "packet_version": "0.1.0",
  "schema_url": "https://clinicbrain.ai/spec/dental-case-packet/v0.1/schema.json"
}
```

The v0.1 reference implementation does not require these fields yet to avoid breaking the initial MVP schema.

## Release Artifacts

Every spec release SHOULD include:

- human-readable Markdown spec
- JSON Schema
- example packets
- changelog
- validator conformance tests

