from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any, Generic, Self, cast, overload

from cmu_graphics.libs.martinez.reprit.base import generate_repr

from .abcs import HasCustomRepr, Node, Tree
from .hints import Item, KeyT, ValueT
from .nil import NIL
from .views import ItemsView, KeysView, ValuesView


class Map(HasCustomRepr, Generic[KeyT, ValueT]):
    __slots__ = ('_tree',)

    def __init__(self, _tree: Tree[KeyT, ValueT], /) -> None:
        self._tree = _tree

    __repr__ = generate_repr(__init__)

    def __contains__(self, key: KeyT, /) -> bool:
        return self._tree.find(key) is not NIL

    def __copy__(self, /) -> Map[KeyT, ValueT]:
        return Map(self._tree.__copy__())

    def __delitem__(self, key: KeyT, /) -> None:
        node = self._tree.pop(key)
        if node is NIL:
            raise KeyError(key)

    @overload
    def __eq__(self, other: Self, /) -> bool: ...

    @overload
    def __eq__(self, other: Any, /) -> Any: ...

    def __eq__(self, other: Any, /) -> Any:
        return (
            self.keys() == other.keys()
            and all(other[key] == value for key, value in self.items())
            if isinstance(other, Map)
            else NotImplemented
        )

    def __getitem__(self, key: KeyT, /) -> ValueT:
        return self._find_node(key).value

    def __iter__(self, /) -> Iterator[KeyT]:
        for node in self._tree:
            yield node.key

    def __len__(self, /) -> int:
        return len(self._tree)

    def __reversed__(self, /) -> Iterator[KeyT]:
        for node in reversed(self._tree):
            yield node.key

    def __setitem__(self, key: KeyT, value: ValueT, /) -> None:
        self._tree.insert(key, value).value = value

    def ceil(self, key: KeyT, /) -> ValueT:
        return self._ceil_node(key).value

    def ceilitem(self, key: KeyT, /) -> Item[KeyT, ValueT]:
        return self._ceil_node(key).item

    def clear(self, /) -> None:
        self._tree.clear()

    def floor(self, key: KeyT, /) -> ValueT:
        return self._floor_node(key).value

    def flooritem(self, key: KeyT, /) -> Item[KeyT, ValueT]:
        return self._floor_node(key).item

    def get(
        self, key: KeyT, default: ValueT | None = None, /
    ) -> ValueT | None:
        return (
            node.value
            if (node := self._tree.find(key)) is not NIL
            else default
        )

    def items(self, /) -> ItemsView[KeyT, ValueT]:
        return ItemsView(self._tree)

    def keys(self, /) -> KeysView[KeyT]:
        return KeysView(self._tree)

    def max(self, /) -> ValueT:
        return self._max_node().value

    def maxitem(self, /) -> Item[KeyT, ValueT]:
        return self._max_node().item

    def min(self, /) -> ValueT:
        return self._min_node().value

    def minitem(self, /) -> Item[KeyT, ValueT]:
        return self._min_node().item

    def next(self, key: KeyT, /) -> ValueT:
        return self._next_node(key).value

    def nextitem(self, key: KeyT, /) -> Item[KeyT, ValueT]:
        return self._next_node(key).item

    __sentinel = cast(ValueT, object())

    @overload
    def pop(self, key: KeyT, /, default: ValueT) -> ValueT: ...

    @overload
    def pop(self, key: KeyT, /, default: ValueT = ...) -> ValueT: ...

    def pop(self, key: KeyT, /, default: ValueT = __sentinel) -> ValueT:
        node = self._tree.pop(key)
        if node is NIL:
            if default is self.__sentinel:
                raise KeyError(key)
            return default
        return node.value

    def popmax(self, /) -> ValueT:
        return self._popmax_node().value

    def popmaxitem(self, /) -> Item[KeyT, ValueT]:
        return self._popmax_node().item

    def popmin(self, /) -> ValueT:
        return self._popmin_node().value

    def popminitem(self, /) -> Item[KeyT, ValueT]:
        return self._popmin_node().item

    popitem = popminitem

    def prev(self, key: KeyT, /) -> ValueT:
        return self._prev_node(key).value

    def previtem(self, key: KeyT, /) -> Item[KeyT, ValueT]:
        return self._prev_node(key).item

    @overload
    def setdefault(
        self: Map[KeyT, ValueT | None], key: KeyT, default: None = ..., /
    ) -> None: ...

    @overload
    def setdefault(self, key: KeyT, default: ValueT, /) -> ValueT: ...

    def setdefault(
        self: Map[KeyT, ValueT | None],
        key: KeyT,
        default: ValueT | None = None,
        /,
    ) -> ValueT | None:
        node = self._tree.find(key)
        return (self._tree.insert(key, default) if node is NIL else node).value

    def update(
        self, other: Self | Iterable[Item[KeyT, ValueT]] = (), /
    ) -> None:
        items = cast(
            Iterable[Item[KeyT, ValueT]],
            other.items() if isinstance(other, Map) else other,
        )
        for key, value in items:
            self[key] = value

    def values(self, /) -> ValuesView[ValueT]:
        return ValuesView(self._tree)

    def _ceil_node(self, key: KeyT, /) -> Node[KeyT, ValueT]:
        node = self._tree.supremum(key)
        if node is NIL:
            raise KeyError(f'No key found greater than or equal to {key!r}')
        return node

    def _find_node(self, key: KeyT, /) -> Node[KeyT, ValueT]:
        result = self._tree.find(key)
        if result is NIL:
            raise KeyError(key)
        return result

    def _floor_node(self, key: KeyT, /) -> Node[KeyT, ValueT]:
        result = self._tree.infimum(key)
        if result is NIL:
            raise KeyError(f'No key found less than or equal to {key!r}')
        return result

    def _max_node(self, /) -> Node[KeyT, ValueT]:
        result = self._tree.max()
        if result is NIL:
            raise KeyError('Map is empty')
        return result

    def _min_node(self, /) -> Node[KeyT, ValueT]:
        result = self._tree.min()
        if result is NIL:
            raise KeyError('Map is empty')
        return result

    def _next_node(self, key: KeyT, /) -> Node[KeyT, ValueT]:
        result = self._tree.successor(self._find_node(key))
        if result is NIL:
            raise KeyError('Corresponds to maximum')
        return result

    def _popmax_node(self, /) -> Node[KeyT, ValueT]:
        result = self._tree.popmax()
        if result is NIL:
            raise KeyError('Map is empty')
        return result

    def _popmin_node(self, /) -> Node[KeyT, ValueT]:
        result = self._tree.popmin()
        if result is NIL:
            raise KeyError('Map is empty')
        return result

    def _prev_node(self, key: KeyT, /) -> Node[KeyT, ValueT]:
        result = self._tree.predecessor(self._find_node(key))
        if result is NIL:
            raise KeyError('Corresponds to minimum')
        return result
