from __future__ import annotations

from typing import Any, Generic, Self, overload

from cmu_graphics.libs.martinez.reprit.base import generate_repr as _generate_repr

from .hints import HasCustomRepr, KeyT, ValueT


class Item(HasCustomRepr, Generic[KeyT, ValueT]):
    key: KeyT
    value: ValueT

    __slots__ = 'key', 'value'

    def __init__(self, key: KeyT, value: ValueT, /) -> None:
        self.key, self.value = key, value

    @overload
    def __eq__(self, other: Self, /) -> bool: ...

    @overload
    def __eq__(self, other: Any, /) -> Any: ...

    def __eq__(self, other: Any, /) -> Any:
        return (
            self.key == other.key and self.value == other.value
            if isinstance(other, Item)
            else NotImplemented
        )

    @overload
    def __lt__(self, other: Self, /) -> bool: ...

    @overload
    def __lt__(self, other: Any, /) -> Any: ...

    def __lt__(self, other: Any, /) -> Any:
        return (
            self.key < other.key if isinstance(other, Item) else NotImplemented
        )

    __repr__ = _generate_repr(__init__)
