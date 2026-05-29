from __future__ import annotations

import pytest

from dental_packet.connectors import LlmConnectorRequest
from dental_packet.context import DentalContext
from dental_packet.ingestion import IngestedRecord, RecordKind
from dental_packet.normalization import NormalizedRecord


def test_target_architecture_scaffolds_importable(tmp_path) -> None:
    source = IngestedRecord(
        path=tmp_path / "scan.stl",
        kind=RecordKind.MESH,
        role="intraoral_scan",
        sha256="abc",
        size_bytes=123,
    )
    normalized = NormalizedRecord(source=source, standard_metadata={"format": "stl"})
    context = DentalContext(case_overview="Non-diagnostic overview.")

    assert normalized.source.kind == RecordKind.MESH
    assert context.known_information == []


def test_llm_connector_request_blocks_diagnosis() -> None:
    request = LlmConnectorRequest(
        provider="openai",
        prompt_context="Summarize records for clinical review only.",
        allow_diagnosis=True,
    )

    with pytest.raises(ValueError, match="must not allow diagnosis"):
        request.validate_safety()

