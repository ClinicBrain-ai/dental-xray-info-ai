# Quickstart

This guide builds and validates a Dental Case Packet from the included sample files.

The reference implementation is local-first. It does not call an LLM API, diagnose, recommend
treatment, or claim clinical accuracy.

## Requirements

- Python 3.11 or newer
- Git

## Install

```bash
git clone https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet.git
cd ai-ready-dental-case-packet

python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Build The Sample Packet

```bash
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
```

Expected output:

```text
Built case packet: case_packet_output/case_packet.json
```

## Validate The Packet

```bash
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

Expected output:

```text
case_packet.json is valid
```

## Inspect The Output

```text
case_packet_output/
  case_packet.json
  case_packet.md
  manifest.json
  files_index.json
  deidentified/
  thumbnails/
  logs/
```

Important files:

- `case_packet.json`: structured AI-ready Dental Case Packet.
- `case_packet.md`: human-readable review report.
- `manifest.json`: indexed source files with SHA-256 hashes.
- `files_index.json`: compact file index.
- `deidentified/`: de-identified text and JSON copies.
- `logs/pipeline.log`: warnings, including PHI field detections without raw PHI values.

## Run Developer Checks

```bash
ruff check .
pytest
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

## Use Your Own Input Folder

Create a folder with any subset of these files:

```text
project-input/
  patient_info.json
  chief_complaint.txt
  clinical_notes.txt
  treatment_plan.txt
  cbct/
    *.dcm
  xray/
    *.dcm or *.jpg or *.png
  intraoral_scan/
    *.stl or *.ply or *.obj
  photos/
    *.jpg or *.png
```

Then run:

```bash
python -m dental_packet build --input ./project-input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

## Safety Notes

- Do not use generated packets as diagnosis.
- Do not use generated packets as treatment recommendations.
- Review all outputs with a licensed dentist before clinical use.
- Keep real patient data local unless your organization has approved storage and sharing policies.
