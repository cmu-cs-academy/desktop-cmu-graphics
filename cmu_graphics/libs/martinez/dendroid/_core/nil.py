from __future__ import annotations

from enum import Enum, auto
from typing import Final, final


@final
class Nil(Enum):
    _VALUE = auto()


NIL: Final = Nil._VALUE  # noqa: SLF001
