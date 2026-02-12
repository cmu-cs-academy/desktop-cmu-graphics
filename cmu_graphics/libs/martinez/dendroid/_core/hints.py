from collections.abc import Callable
from typing import Any, TypeAlias, Self, TypeVar, Protocol


class Ordered(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...


KeyT = TypeVar('KeyT', bound=Ordered)
ValueT = TypeVar('ValueT', bound=Any)
Order: TypeAlias = Callable[[ValueT], KeyT]
Item: TypeAlias = tuple[KeyT, ValueT]
