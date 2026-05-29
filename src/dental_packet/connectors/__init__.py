"""Optional LLM connector contracts.

Connectors must preserve the non-diagnostic safety boundary. They should prepare prompts or
requests, not diagnose or recommend treatment.
"""

from dental_packet.connectors.base import LlmConnectorRequest

__all__ = ["LlmConnectorRequest"]

