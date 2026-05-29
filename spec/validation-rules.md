# Validation Rules

Status: Draft  
Applies to: Dental Case Packet v0.1

## Validator Modes

### Strict Mode

Strict validators MUST:

- enforce the JSON Schema
- reject unknown top-level fields
- require all safety flags to be `true`
- reject packets that embed large binary payloads
- reject known PHI DICOM fields in packet metadata
- reject missing `llm_prompt_context`

### Advisory Mode

Advisory validators MAY:

- accept vendor extensions
- emit warnings instead of hard failures for non-critical metadata omissions
- accept unknown nested fields in file references
- produce remediation hints

## Required Hard Failures

A validator MUST fail when:

1. The packet is not valid JSON.
2. Required fields are missing.
3. `patient.deidentified` is not `true`.
4. `safety.not_for_diagnosis` is not `true`.
5. `safety.requires_dentist_review` is not `true`.
6. `safety.phi_removed` is not `true`.
7. `llm_prompt_context` asks for diagnosis or treatment recommendations.
8. The packet contains raw binary imaging content.
9. Known DICOM PHI field names appear with raw values.
10. `case_id` contains obvious direct identifiers.

## Recommended Warnings

A validator SHOULD warn when:

- filenames appear to contain names, phone numbers, emails, dates of birth, or patient IDs
- DICOM pixel data may contain burned-in annotations
- photos are present
- PDFs are present
- free text contains dates or contact patterns
- no source manifest is available
- no content hashes are available
- `missing_information` is empty despite absent imaging categories

## Non-Diagnostic Language Checks

The validator SHOULD check that AI-facing context includes phrases equivalent to:

- "Do not diagnose"
- "Do not provide treatment recommendations"
- "For clinical review only"
- "Requires dentist review"

Validators SHOULD NOT rely only on exact phrase matching in future versions. Semantic safety classifiers may be introduced as advisory validators.

## Privacy Checks

Validators MUST NOT print raw PHI in validation output. If a field fails privacy validation, the validator should report:

```json
{
  "code": "PHI_FIELD_DETECTED",
  "path": "$.imaging.cbct.dicom_metadata_summary",
  "message": "Known PHI field detected. Raw value suppressed."
}
```

## Compatibility Checks

Validators SHOULD expose:

- `spec_version`
- `schema_id`
- `validator_version`
- `mode`
- `errors`
- `warnings`

