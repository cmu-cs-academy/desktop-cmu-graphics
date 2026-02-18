from __future__ import annotations

from collections.abc import Collection, Iterable, Iterator, Set
from typing import Any, Self

from cmu_graphics.libs.martinez.reprit.base import generate_repr

from . import abcs
from .hints import Item, KeyT, ValueT
from .nil import NIL
from .utils import split_items


class ItemsView(abcs.HasCustomRepr, abcs.AbstractSet[Item[KeyT, ValueT]]):
    def from_iterable(self, value: Iterable[Item[KeyT, ValueT]], /) -> Self:
        keys, values = split_items(list(value))
        return type(self)(self._tree.from_components(keys, values))

    __slots__ = ('_tree',)

    def __contains__(self, item: Item[KeyT, ValueT], /) -> bool:
        key, value = item
        node = self._tree.find(key)
        return node is not NIL and node.value == value

    def __init__(self, _tree: abcs.Tree[KeyT, ValueT], /) -> None:
        self._tree = _tree

    def __iter__(self, /) -> Iterator[Item[KeyT, ValueT]]:
        for node in self._tree:
            yield node.item

    def __len__(self, /) -> int:
        return len(self._tree)

    __repr__ = generate_repr(__init__)

    def __reversed__(self, /) -> Iterator[Item[KeyT, ValueT]]:
        for node in reversed(self._tree):
            yield node.item


class KeysView(abcs.HasCustomRepr, abcs.AbstractSet[KeyT]):
    def from_iterable(self, _value: Iterable[KeyT], /) -> KeysView[KeyT]:
        return KeysView(self._tree.from_components(_value))

    __slots__ = ('_tree',)

    def __contains__(self, key: KeyT, /) -> bool:
        return self._tree.find(key) is not NIL

    def __init__(self, _tree: abcs.Tree[KeyT, Any], /) -> None:
        self._tree = _tree

    def __iter__(self, /) -> Iterator[KeyT]:
        for node in self._tree:
            yield node.key

    def __len__(self, /) -> int:
        return len(self._tree)

    __repr__ = generate_repr(__init__)

    def __reversed__(self, /) -> Iterator[KeyT]:
        for node in reversed(self._tree):
            yield node.key


class ValuesView(abcs.HasCustomRepr, abcs.Collection[ValueT]):
    __slots__ = ('_tree',)

    def __contains__(self, value: ValueT, /) -> bool:
        return any(candidate == value for candidate in self)

    def __init__(self, _tree: abcs.Tree[KeyT, ValueT], /) -> None:
        self._tree = _tree

    def __iter__(self, /) -> Iterator[ValueT]:
        for node in self._tree:
            yield node.value

    def __len__(self, /) -> int:
        return len(self._tree)

    __repr__ = generate_repr(__init__)

    def __reversed__(self, /) -> Iterator[ValueT]:
        for node in reversed(self._tree):
            yield node.value


Set.register(ItemsView)  # pyright: ignore[reportAttributeAccessIssue]
Set.register(KeysView)  # pyright: ignore[reportAttributeAccessIssue]
Collection.register(ItemsView)  # pyright: ignore[reportAttributeAccessIssue]
