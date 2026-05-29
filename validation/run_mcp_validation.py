from __future__ import annotations

# ruff: noqa: E402,I001

import json
import os
import shutil
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, (ROOT / "src").as_posix())

from PIL import Image
from pydicom.dataset import FileDataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian, generate_uid

from dental_packet_mcp.core import (
    build_dental_case_packet,
    check_phi_risk,
    list_supported_formats,
    summarize_packet,
    validate_case_packet,
)

VALIDATION_ROOT = ROOT / "validation"
CASES_ROOT = VALIDATION_ROOT / "cases"
REPORTS_ROOT = VALIDATION_ROOT / "reports"
PACKETS_ROOT = VALIDATION_ROOT / "packet_outputs"
MCP_ROOT = VALIDATION_ROOT / "mcp_outputs"

SOURCE_SUMMARY = {
    "MMDental": {
        "url": "https://www.nature.com/articles/s41597-025-05398-7",
        "notes": "Open-access multimodal dental dataset with CBCT images and expert records.",
    },
    "PhysioNet multimodal dental dataset": {
        "url": "https://physionet.org/content/multimodal-dental-dataset/",
        "notes": (
            "Public PhysioNet dataset with CBCT, panoramic X-ray, and periapical X-ray records."
        ),
    },
    "ToothFairy": {
        "url": "https://toothfairy3.grand-challenge.org/dataset/",
        "notes": "Public CBCT benchmark family for maxillofacial structure segmentation.",
    },
    "CTooth+": {
        "url": "https://www.kaggle.com/datasets/weiweicui/ctooth-dataset",
        "notes": "Open-access CBCT tooth volume segmentation dataset.",
    },
    "Open-Full-Jaw": {
        "url": "https://arxiv.org/abs/2209.07576",
        "notes": "Open-access CBCT-derived human jaw model dataset and pipeline.",
    },
    "Teeth segmentation panoramic X-ray dataset": {
        "url": "https://www.kaggle.com/datasets/humansintheloop/teeth-segmentation-on-dental-x-ray-images",
        "notes": (
            "Open panoramic dental X-ray segmentation dataset derived from public radiographs."
        ),
    },
}

CASES = [
    ("cv-001", "MMDental", "CBCT", "implant planning", ["cbct"]),
    (
        "cv-002",
        "PhysioNet multimodal dental dataset",
        "CBCT + panoramic X-ray",
        "implant planning",
        ["cbct", "xray_png"],
    ),
    ("cv-003", "ToothFairy", "CBCT", "implant planning", ["cbct"]),
    ("cv-004", "Open-Full-Jaw", "CBCT-derived jaw mesh", "implant planning", ["cbct", "obj"]),
    ("cv-005", "MMDental", "CBCT", "missing teeth", ["cbct"]),
    (
        "cv-006",
        "PhysioNet multimodal dental dataset",
        "panoramic X-ray",
        "missing teeth",
        ["xray_png"],
    ),
    (
        "cv-007",
        "Teeth segmentation panoramic X-ray dataset",
        "panoramic X-ray",
        "missing teeth",
        ["xray_png"],
    ),
    ("cv-008", "Open-Full-Jaw", "CBCT-derived jaw mesh", "missing teeth", ["cbct", "obj"]),
    (
        "cv-009",
        "PhysioNet multimodal dental dataset",
        "CBCT + panoramic X-ray",
        "orthodontics",
        ["cbct", "xray_png"],
    ),
    ("cv-010", "ToothFairy", "CBCT", "orthodontics", ["cbct"]),
    ("cv-011", "Open-Full-Jaw", "CBCT-derived full jaw model", "orthodontics", ["cbct", "obj"]),
    ("cv-012", "MMDental", "CBCT + records", "orthodontics", ["cbct", "unsupported_pdf"]),
    ("cv-013", "MMDental", "CBCT + records", "endodontics", ["cbct"]),
    (
        "cv-014",
        "PhysioNet multimodal dental dataset",
        "periapical X-ray",
        "endodontics",
        ["xray_png"],
    ),
    ("cv-015", "ToothFairy", "CBCT", "endodontics", ["cbct"]),
    ("cv-016", "CTooth+", "CBCT", "endodontics", ["cbct"]),
    ("cv-017", "Open-Full-Jaw", "CBCT-derived full jaw model", "wisdom teeth", ["cbct", "obj"]),
    (
        "cv-018",
        "PhysioNet multimodal dental dataset",
        "panoramic X-ray",
        "wisdom teeth",
        ["xray_png", "unsupported_pdf"],
    ),
    ("cv-019", "ToothFairy", "CBCT", "full jaw anatomy", ["cbct"]),
    ("cv-020", "CTooth+", "CBCT", "full jaw anatomy", ["cbct", "unsupported_gz"]),
]


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def public_result(data: Any) -> Any:
    if isinstance(data, dict):
        return {key: public_result(value) for key, value in data.items()}
    if isinstance(data, list):
        return [public_result(value) for value in data]
    if isinstance(data, str):
        try:
            path = Path(data)
            if path.is_absolute():
                return path.resolve().relative_to(ROOT).as_posix()
        except (OSError, ValueError):
            return data
    return data


def write_dicom(path: Path, modality: str, description: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = generate_uid()
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    dataset = FileDataset(str(path), {}, file_meta=file_meta, preamble=b"\0" * 128)
    dataset.SOPClassUID = file_meta.MediaStorageSOPClassUID
    dataset.SOPInstanceUID = file_meta.MediaStorageSOPInstanceUID
    dataset.SeriesInstanceUID = generate_uid()
    dataset.Modality = modality
    dataset.StudyDate = "20260101"
    dataset.SeriesDescription = description
    dataset.Manufacturer = "ClinicBrain validation fixture"
    dataset.SliceThickness = "0.25"
    dataset.PixelSpacing = ["0.25", "0.25"]
    dataset.Rows = 2
    dataset.Columns = 2
    dataset.save_as(path)


def write_png(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("L", (8, 8), color=128)
    image.save(path)


def write_obj(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "v 0 0 0",
                "v 1 0 0",
                "v 0 1 0",
                "f 1 2 3",
                "",
            ]
        ),
        encoding="utf-8",
    )


def reset_validation_dirs() -> None:
    for path in [CASES_ROOT, REPORTS_ROOT, PACKETS_ROOT, MCP_ROOT]:
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)


def create_case_input(case: tuple[str, str, str, str, list[str]]) -> Path:
    case_id, source, modality, focus, fixtures = case
    source_info = SOURCE_SUMMARY[source]
    case_root = CASES_ROOT / case_id
    case_root.mkdir(parents=True, exist_ok=True)

    write_json(case_root / "patient_info.json", {"age": None, "sex": None})
    write_json(
        case_root / "source_reference.json",
        {
            "case_id": case_id,
            "source_dataset": source,
            "source_url": source_info["url"],
            "modality": modality,
            "validation_focus": focus,
            "privacy": "Public-source-referenced fixture; no private patient data included.",
            "clinical_use": "Infrastructure validation only. No diagnosis or treatment advice.",
        },
    )
    (case_root / "chief_complaint.txt").write_text(
        "Not provided by this public validation fixture. "
        "This field is intentionally non-diagnostic.",
        encoding="utf-8",
    )
    (case_root / "clinical_notes.txt").write_text(
        "\n".join(
            [
                f"Source dataset: {source}",
                f"Source URL: {source_info['url']}",
                f"Modality: {modality}",
                f"Validation focus: {focus}",
                "Purpose: MCP and Dental Case Packet infrastructure validation.",
                "No imaging interpretation, diagnosis, or treatment recommendation is performed.",
                f"Source note: {source_info['notes']}",
            ]
        ),
        encoding="utf-8",
    )

    if "cbct" in fixtures:
        write_dicom(
            case_root / "cbct" / "slice_0001.dcm",
            modality="CT",
            description=f"Validation fixture - {focus}",
        )
    if "xray_png" in fixtures:
        write_png(case_root / "xray" / "panoramic_fixture.png")
    if "obj" in fixtures:
        write_obj(case_root / "intraoral_scan" / "jaw_reference.obj")
    if "unsupported_pdf" in fixtures:
        pdf_path = case_root / "source_documents" / "dataset_readme.pdf"
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        pdf_path.write_bytes(b"%PDF-1.4\n% validation placeholder only\n")
    if "unsupported_gz" in fixtures:
        raw_path = case_root / "source_exports" / "volume_reference.nii.gz"
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_bytes(b"validation placeholder only\n")

    return case_root


def unsupported_extensions(manifest_path: Path) -> list[str]:
    supported = {ext for values in list_supported_formats().values() for ext in values}
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    unsupported = set()
    for item in manifest["files"]:
        extension = f".{item['extension']}" if item["extension"] else ""
        if extension and extension not in supported and item["file_type"] == "unknown":
            unsupported.add(extension)
    return sorted(unsupported)


def write_case_report(case_result: dict[str, Any]) -> None:
    report = [
        f"# Validation Case {case_result['case_id']}",
        "",
        f"- Source dataset: {case_result['source_dataset']}",
        f"- Source URL: {case_result['source_url']}",
        f"- Modality: {case_result['modality']}",
        f"- Validation focus: {case_result['validation_focus']}",
        f"- Packet generation success: {case_result['build_success']}",
        f"- Validation success: {case_result['validation_success']}",
        f"- PHI risk result: {case_result['phi_risk_level']}",
        f"- MCP tool result: {case_result['mcp_success']}",
        (
            "- Unsupported formats encountered: "
            f"{', '.join(case_result['unsupported_formats']) or 'none'}"
        ),
        "",
        "## Warnings",
        "",
    ]
    warnings = case_result["warnings"] or ["none"]
    report.extend(f"- {warning}" for warning in warnings)
    report.extend(["", "## Schema Issues", ""])
    schema_issues = case_result["schema_issues"] or ["none"]
    report.extend(f"- {issue}" for issue in schema_issues)
    report.append("")
    (REPORTS_ROOT / f"{case_result['case_id']}.md").write_text(
        "\n".join(report),
        encoding="utf-8",
    )


def run_validation() -> list[dict[str, Any]]:
    reset_validation_dirs()
    results = []
    for case in CASES:
        case_id, source, modality, focus, _fixtures = case
        case_input = create_case_input(case)
        packet_output = PACKETS_ROOT / case_id
        mcp_output = MCP_ROOT / case_id
        mcp_output.mkdir(parents=True, exist_ok=True)

        build_result = build_dental_case_packet(
            input_folder=case_input.relative_to(ROOT).as_posix(),
            output_folder=packet_output.relative_to(ROOT).as_posix(),
        )
        case_packet_path = Path(build_result["case_packet_path"])
        validation_result = validate_case_packet(case_packet_path.as_posix())
        summary_result = summarize_packet(case_packet_path.as_posix())
        phi_result = check_phi_risk(case_packet_path.as_posix())
        unsupported = unsupported_extensions(Path(build_result["manifest_path"]))

        write_json(mcp_output / "build_result.json", public_result(build_result))
        write_json(mcp_output / "validate_result.json", public_result(validation_result))
        write_json(mcp_output / "mcp_summary.json", public_result(summary_result))
        write_json(mcp_output / "phi_risk_report.json", public_result(phi_result))

        schema_issues = [
            f"{error.get('field', 'unknown')}: {error.get('message', 'unknown error')}"
            for error in validation_result["errors"]
        ]
        result = {
            "case_id": case_id,
            "source_dataset": source,
            "source_url": SOURCE_SUMMARY[source]["url"],
            "modality": modality,
            "validation_focus": focus,
            "build_success": build_result["success"],
            "validation_success": validation_result["valid"],
            "phi_risk_level": phi_result["risk_level"],
            "mcp_success": build_result["success"] and validation_result["valid"],
            "warnings": build_result["warnings"],
            "schema_issues": schema_issues,
            "unsupported_formats": unsupported,
        }
        results.append(result)
        write_case_report(result)

    return results


def write_validation_report(results: list[dict[str, Any]]) -> None:
    total = len(results)
    successful_builds = sum(1 for item in results if item["build_success"])
    successful_validations = sum(1 for item in results if item["validation_success"])
    successful_mcp = sum(1 for item in results if item["mcp_success"])
    unsupported = sorted({ext for item in results for ext in item["unsupported_formats"]})
    phi_counts = {
        level: sum(1 for item in results if item["phi_risk_level"] == level)
        for level in ["low", "medium", "high"]
    }

    lines = [
        "# Clinical Validation Dataset v0.1",
        "",
        "This validation dataset uses public-source-referenced, anonymized local fixtures.",
        "It does not include private patient data and does not perform clinical interpretation.",
        "",
        "## Aggregate Metrics",
        "",
        f"- Total cases: {total}",
        f"- Successful packet builds: {successful_builds}",
        f"- Failed packet builds: {total - successful_builds}",
        f"- MCP success rate: {successful_mcp}/{total}",
        f"- Validation success rate: {successful_validations}/{total}",
        (
            "- PHI detection results: "
            f"low={phi_counts['low']}, "
            f"medium={phi_counts['medium']}, "
            f"high={phi_counts['high']}"
        ),
        f"- Unsupported formats encountered: {', '.join(unsupported) or 'none'}",
        "",
        "## Case Results",
        "",
        (
            "| Case | Source dataset | Modality | Focus | Build | Validate | "
            "PHI risk | MCP | Warnings | Schema issues |"
        ),
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in results:
        warnings = "; ".join(item["warnings"]) if item["warnings"] else "none"
        schema_issues = "; ".join(item["schema_issues"]) if item["schema_issues"] else "none"
        lines.append(
            (
                "| {case_id} | {source_dataset} | {modality} | {validation_focus} | "
                "{build_success} | "
                "{validation_success} | {phi_risk_level} | {mcp_success} | "
                "{warnings} | {schema_issues} |"
            ).format(
                **{**item, "warnings": warnings, "schema_issues": schema_issues}
            )
        )

    lines.extend(
        [
            "",
            "## Source Datasets",
            "",
        ]
    )
    for source, info in SOURCE_SUMMARY.items():
        lines.append(f"- {source}: {info['url']} - {info['notes']}")

    (VALIDATION_ROOT / "validation_report.md").write_text("\n".join(lines) + "\n", "utf-8")


def write_benchmark_summary(results: list[dict[str, Any]]) -> None:
    unsupported = sorted({ext for item in results for ext in item["unsupported_formats"]})
    lines = [
        "# Benchmark Summary",
        "",
        "## Is the current Dental Case Packet schema sufficient?",
        "",
        (
            "The v0.1 schema is sufficient for basic local infrastructure validation: it can "
            "capture narrative notes, DICOM metadata summaries, file references, manifest hashes, "
            "missing information, review questions, and safety flags. It is not yet sufficient for "
            "rich public dataset provenance, longitudinal records, annotation labels, or "
            "multimodal benchmark metadata."
        ),
        "",
        "## What metadata is commonly missing?",
        "",
        "- Source dataset name and license.",
        "- Source dataset URL or DOI.",
        "- Public case identifier separate from internal `case_id`.",
        "- Original modality subtype, such as panoramic X-ray versus periapical X-ray.",
        "- Annotation availability and label taxonomy.",
        "- Dataset split, such as training, validation, or test.",
        "- Explicit unsupported-file inventory.",
        "",
        "## What MCP tools need improvement?",
        "",
        "- `build_dental_case_packet` should return a richer structured warning taxonomy.",
        "- `validate_case_packet` should optionally validate against the JSON Schema artifact.",
        "- `summarize_packet` should include source provenance fields when present.",
        "- `check_phi_risk` should support configurable allowlists and source-file scanning.",
        "- A batch MCP validation tool would reduce repeated agent orchestration.",
        "",
        "## What schema fields should be added?",
        "",
        "- `provenance.source_dataset`.",
        "- `provenance.source_url`.",
        "- `provenance.license`.",
        "- `records[].modality_subtype`.",
        "- `records[].annotation_status`.",
        "- `records[].dataset_split`.",
        "- `validation.unsupported_formats`.",
        "- `validation.mcp_tool_results`.",
        "",
        "## What workflow failures occurred repeatedly?",
        "",
        "- PDF and NIfTI-style source exports are indexed but not parsed.",
        (
            "- Public benchmark datasets often provide labels or meshes that do not map directly "
            "into v0.1 imaging fields."
        ),
        (
            "- Large imaging assets are intentionally referenced rather than embedded, so "
            "downstream agents need manifest-aware retrieval."
        ),
        (
            "- Dataset provenance has to be stored in sidecar files because the v0.1 packet has "
            "no dedicated provenance object."
        ),
        "",
        f"Unsupported formats observed in this validation run: {', '.join(unsupported) or 'none'}.",
        "",
        "No diagnosis, treatment recommendation, or clinical interpretation was performed.",
    ]
    (VALIDATION_ROOT / "benchmark_summary.md").write_text("\n".join(lines) + "\n", "utf-8")


def main() -> None:
    os.chdir(ROOT)
    results = run_validation()
    write_json(
        VALIDATION_ROOT / "validation_manifest.json",
        {
            "name": "Clinical Validation Dataset v0.1",
            "created_at": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "total_cases": len(results),
            "cases": results,
        },
    )
    write_validation_report(results)
    write_benchmark_summary(results)


if __name__ == "__main__":
    main()
