from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable, Iterator
from typing import Any, Generic, Self

from cmu_graphics.libs.martinez.reprit.base import generate_repr

from .abcs import HasCustomRepr, MutableSet, Tree, TreeWrapper
from .hints import KeyT, Order, ValueT
from .nil import NIL


class BaseSet(TreeWrapper[Any, ValueT], MutableSet[ValueT]):
    @abstractmethod
    def ceil(self, value: ValueT, /) -> ValueT:
        """Returns first value not less than the given one."""

    def clear(self, /) -> None:
        self._tree.clear()

    @abstractmethod
    def floor(self, value: ValueT, /) -> ValueT:
        """Returns first value not greater than the given one."""

    def max(self, /) -> ValueT:
        node = self._tree.max()
        if node is NIL:
            raise ValueError('Set is empty')
        return node.value

    def min(self, /) -> ValueT:
        node = self._tree.min()
        if node is NIL:
            raise ValueError('Set is empty')
        return node.value

    @abstractmethod
    def next(self, value: ValueT, /) -> ValueT:
        """Returns first value greater than the given one."""
        raise NotImplementedError

    def popmax(self, /) -> ValueT:
        node = self._tree.popmax()
        if node is NIL:
            raise ValueError('Set is empty')
        return node.value

    def popmin(self, /) -> ValueT:
        node = self._tree.popmin()
        if node is NIL:
            raise ValueError('Set is empty')
        return node.value

    pop = popmin

    @abstractmethod
    def prev(self, value: ValueT, /) -> ValueT:
        """Returns last value lesser than the given one."""
        raise NotImplementedError

    __slots__ = ()

    def __iter__(self, /) -> Iterator[ValueT]:
        for node in self._tree:
            yield node.value

    def __len__(self, /) -> int:
        return len(self._tree)

    def __reversed__(self, /) -> Iterator[ValueT]:
        for node in reversed(self._tree):
            yield node.value


class Set(HasCustomRepr, BaseSet[ValueT]):
    @property
    def _tree(self, /) -> Tree[Any, ValueT]:
        return self.__tree

    def add(self, value: ValueT, /) -> None:
        self.__tree.insert(value, value)

    def ceil(self, value: ValueT, /) -> ValueT:
        node = self.__tree.supremum(value)
        if node is NIL:
            raise ValueError(
                f'No value found greater than or equal to {value!r}'
            )
        return node.value

    def discard(self, value: ValueT, /) -> None:
        node = self.__tree.find(value)
        if node is NIL:
            return
        self.__tree.remove(node)

    def floor(self, value: ValueT, /) -> ValueT:
        node = self.__tree.infimum(value)
        if node is NIL:
            raise ValueError(f'No value found less than or equal to {value!r}')
        return node.value

    def from_iterable(self, value: Iterable[KeyT], /) -> Set[KeyT]:
        return Set(self.__tree.from_components(value))

    def next(self, value: ValueT, /) -> ValueT:
        node = self.__tree.find(value)
        if node is NIL:
            raise ValueError(f'{value!r} is not in set')
        node = self.__tree.successor(node)
        if node is NIL:
            raise ValueError('Corresponds to maximum')
        return node.value

    def prev(self, value: ValueT, /) -> ValueT:
        node = self.__tree.find(value)
        if node is NIL:
            raise ValueError(f'{value!r} is not in set')
        node = self.__tree.predecessor(node)
        if node is NIL:
            raise ValueError('Corresponds to minimum')
        return node.value

    def remove(self, value: ValueT, /) -> None:
        node = self.__tree.pop(value)
        if node is NIL:
            raise ValueError(f'{value!r} is not in set')

    __slots__ = ('__tree',)

    def __contains__(self, value: ValueT, /) -> bool:
        return self.__tree.find(value) is not NIL

    def __copy__(self, /) -> Self:
        return type(self)(self.__tree.__copy__())

    def __init__(self, _tree: Tree[Any, ValueT], /) -> None:
        self.__tree = _tree

    __repr__ = generate_repr(__init__)


class KeyedSet(HasCustomRepr, Generic[KeyT, ValueT], BaseSet[ValueT]):
    @property
    def key(self, /) -> Order[ValueT, KeyT]:
        return self._key

    @property
    def _tree(self, /) -> Tree[KeyT, ValueT]:
        return self.__tree

    def add(self, value: ValueT, /) -> None:
        self.__tree.insert(self._key(value), value)

    def ceil(self, value: ValueT, /) -> ValueT:
        node = self.__tree.supremum(self._key(value))
        if node is NIL:
            raise ValueError(
                f'No value found greater than or equal to {value!r}'
            )
        return node.value

    def discard(self, value: ValueT, /) -> None:
        node = self.__tree.find(self._key(value))
        if node is NIL:
            return
        self.__tree.remove(node)

    def floor(self, value: ValueT, /) -> ValueT:
        node = self.__tree.infimum(self._key(value))
        if node is NIL:
            raise ValueError(f'No value found less than or equal to {value!r}')
        return node.value

    def from_iterable(
        self, _value: Iterable[ValueT], /
    ) -> KeyedSet[KeyT, ValueT]:
        values = list(_value)
        return KeyedSet(
            self.__tree.from_components(map(self._key, values), values),
            self._key,
        )

    def next(self, value: ValueT, /) -> ValueT:
        key = self._key(value)
        node = self.__tree.find(key)
        if node is NIL:
            raise ValueError(f'{value!r} is not in set')
        node = self.__tree.successor(node)
        if node is NIL:
            raise ValueError('Corresponds to maximum')
        return node.value

    def prev(self, value: ValueT, /) -> ValueT:
        key = self._key(value)
        node = self.__tree.find(key)
        if node is NIL:
            raise ValueError(f'{value!r} is not in set')
        node = self.__tree.predecessor(node)
        if node is NIL:
            raise ValueError('Corresponds to minimum')
        return node.value

    def remove(self, value: ValueT, /) -> None:
        node = self.__tree.pop(self._key(value))
        if node is NIL:
            raise ValueError(f'{value!r} is not in set')

    __slots__ = '__tree', '_key'

    def __contains__(self, value: ValueT, /) -> bool:
        return (
            bool(self.__tree) and self.__tree.find(self._key(value)) is not NIL
        )

    def __copy__(self, /) -> Self:
        return type(self)(self.__tree.__copy__(), self._key)

    def __init__(
        self, _tree: Tree[KeyT, ValueT], key: Order[ValueT, KeyT], /
    ) -> None:
        self._key, self.__tree = key, _tree

    __repr__ = generate_repr(__init__)
