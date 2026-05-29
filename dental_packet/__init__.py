"""Source-tree compatibility package.

The reference implementation lives under ``src/dental_packet``. This small package lets
``python -m dental_packet`` work from a fresh repository checkout before editable install.
"""

from pathlib import Path

_SRC_PACKAGE = Path(__file__).resolve().parent.parent / "src" / "dental_packet"

if _SRC_PACKAGE.exists():
    __path__.append(str(_SRC_PACKAGE))  # type: ignore[name-defined]

__version__ = "0.1.0"

