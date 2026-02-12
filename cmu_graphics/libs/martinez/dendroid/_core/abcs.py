from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator, Sequence
from itertools import chain
from typing import Any, Generic, TypeVar, Self, Protocol, overload

from cmu_graphics.libs.martinez.reprit.base import generate_repr

from .hints import Item, KeyT, Ordered, ValueT
from .nil import NIL, Nil
from .utils import capacity

_KeyT_co = TypeVar('_KeyT_co', bound=Ordered, covariant=True)


class Node(Protocol[_KeyT_co, ValueT]):
    @property
    @abstractmethod
    def left(self, /) -> Self | Nil:
        """Left child."""

    @left.setter
    @abstractmethod
    def left(self, value: Self | Nil, /) -> None:
        """Sets left child."""

    @property
    @abstractmethod
    def right(self, /) -> Self | Nil:
        """Right child."""

    @right.setter
    @abstractmethod
    def right(self, value: Self | Nil, /) -> None:
        """Sets right child."""

    @property
    def item(self, /) -> Item[_KeyT_co, ValueT]:
        return self.key, self.value

    @property
    @abstractmethod
    def key(self, /) -> _KeyT_co:
        """Comparisons key."""

    @property
    @abstractmethod
    def value(self, /) -> ValueT:
        """Underlying value."""

    @value.setter
    @abstractmethod
    def value(self, value: ValueT, /) -> None:
        """Sets underlying value."""

    __slots__ = ()


class HasCustomRepr(Protocol):
    __slots__ = ()

    @abstractmethod
    def __repr__(self, /) -> str:
        raise NotImplementedError


class Tree(ABC, HasCustomRepr, Generic[KeyT, ValueT]):
    @property
    @abstractmethod
    def root(self, /) -> Node[KeyT, ValueT] | Nil:
        raise NotImplementedError

    @overload
    @classmethod
    def from_components(
        cls, keys: Iterable[KeyT], values: None = ..., /
    ) -> Tree[KeyT, KeyT]: ...

    @overload
    @classmethod
    def from_components(
        cls, keys: Iterable[KeyT], values: Iterable[ValueT], /
    ) -> Self: ...

    @classmethod
    @abstractmethod
    def from_components(
        cls: type[Tree[KeyT, KeyT]] | type[Tree[KeyT, ValueT]],
        keys: Iterable[KeyT],
        values: Iterable[ValueT] | None = None,
        /,
    ) -> Tree[KeyT, KeyT] | Tree[KeyT, ValueT]:
        """Constructs tree from given components."""

    @property
    def keys(self, /) -> Sequence[KeyT]:
        return [node.key for node in self]

    @property
    def values(self, /) -> Sequence[ValueT]:
        return [node.value for node in self]

    @abstractmethod
    def clear(self, /) -> None:
        raise NotImplementedError

    def find(self, key: KeyT, /) -> Node[KeyT, ValueT] | Nil:
        """Searches for the node corresponding to a key."""
        node = self.root
        while node is not NIL:
            if key < node.key:
                node = node.left
            elif node.key < key:
                node = node.right
            else:
                break
        return node

    def infimum(self, key: KeyT, /) -> Node[KeyT, ValueT] | Nil:
        """Returns first node with a key not greater than the given one."""
        result: Node[KeyT, ValueT] | Nil
        node, result = self.root, NIL
        while node is not NIL:
            if key < node.key:
                node = node.left
            elif node.key < key:
                result, node = node, node.right
            else:
                result = node
                break
        return result

    @abstractmethod
    def insert(self, key: KeyT, value: ValueT, /) -> Node[KeyT, ValueT]:
        """Inserts given key-value pair in the tree."""

    def max(self, /) -> Node[KeyT, ValueT] | Nil:
        """Returns node with the maximum key."""
        node = self.root
        if node is not NIL:
            while node.right is not NIL:
                node = node.right
        return node

    def min(self, /) -> Node[KeyT, ValueT] | Nil:
        """Returns node with the minimum key."""
        node = self.root
        if node is not NIL:
            while node.left is not NIL:
                node = node.left
        return node

    def pop(self, key: KeyT, /) -> Node[KeyT, ValueT] | Nil:
        """Removes node with given key from the tree."""
        node = self.find(key)
        if node is not NIL:
            self.remove(node)
        return node

    def popmin(self, /) -> Node[KeyT, ValueT] | Nil:
        node = self.root
        if node is not NIL:
            while node.left is not NIL:
                node = node.left
            self.remove(node)
        return node

    def popmax(self, /) -> Node[KeyT, ValueT] | Nil:
        node = self.root
        if node is not NIL:
            while node.right is not NIL:
                node = node.right
            self.remove(node)
        return node

    @abstractmethod
    def predecessor(
        self, node: Node[KeyT, ValueT], /
    ) -> Node[KeyT, ValueT] | Nil:
        """Returns last node with a key less than of the given one."""

    @abstractmethod
    def remove(self, node: Node[KeyT, ValueT], /) -> None:
        """Removes node from the tree."""

    @abstractmethod
    def successor(
        self, node: Node[KeyT, ValueT], /
    ) -> Node[KeyT, ValueT] | Nil:
        """Returns first node with a key greater than of the given one."""

    def supremum(self, key: KeyT, /) -> Node[KeyT, ValueT] | Nil:
        """Returns first node with a key not less than the given one."""
        result: Node[KeyT, ValueT] | Nil
        node, result = self.root, NIL
        while node is not NIL:
            if key < node.key:
                result, node = node, node.left
            elif node.key < key:
                node = node.right
            else:
                result = node
                break
        return result

    __slots__ = ()

    def __bool__(self, /) -> bool:
        """Checks if the tree has nodes."""
        return self.root is not NIL

    @abstractmethod
    def __copy__(self, /) -> Self:
        raise NotImplementedError

    def __iter__(self, /) -> Iterator[Node[KeyT, ValueT]]:
        """Returns iterator over nodes in ascending keys order."""
        node = self.root
        queue = []
        while True:
            while node is not NIL:
                queue.append(node)
                node = node.left
            if not queue:
                return
            node = queue.pop()
            yield node
            node = node.right

    def __len__(self, /) -> int:
        """Returns number of nodes."""
        return capacity(self)

    __repr__ = generate_repr(from_components, with_module_name=True)

    def __reversed__(self, /) -> Iterator[Node[KeyT, ValueT]]:
        """Returns iterator over nodes in descending keys order."""
        node = self.root
        queue = []
        while True:
            while node is not NIL:
                queue.append(node)
                node = node.right
            if not queue:
                return
            node = queue.pop()
            yield node
            node = node.left


class Collection(ABC, Generic[ValueT]):
    __slots__ = ()

    @abstractmethod
    def __contains__(self, value: ValueT, /) -> bool:
        """Checks if given value is presented in the set."""
        raise NotImplementedError

    @abstractmethod
    def __iter__(self, /) -> Iterator[ValueT]:
        """Returns iterator over the set values."""
        raise NotImplementedError

    @abstractmethod
    def __len__(self, /) -> int:
        """Returns size of the set."""
        raise NotImplementedError


class AbstractSet(Collection[ValueT]):
    @abstractmethod
    def from_iterable(self, value: Iterable[ValueT], /) -> Self:
        """Constructs set from given values."""

    def isdisjoint(self, other: Iterable[ValueT], /) -> bool:
        """Checks if the tree share no values with given iterable."""
        return all(value not in self for value in other)

    __slots__ = ()

    def __and__(self, other: AbstractSet[ValueT], /) -> Self:
        """Returns intersection of the set with given one."""
        return (
            self.from_iterable(value for value in self if value in other)
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    @overload
    def __eq__(self, other: Self, /) -> bool: ...

    @overload
    def __eq__(self, other: Any, /) -> Any: ...

    def __eq__(self, other: Any, /) -> Any:
        """Checks if the set is equal to given one."""
        return (
            len(self) == len(other) and self <= other <= self
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    @overload
    def __ge__(self, other: Self, /) -> bool: ...

    @overload
    def __ge__(self, other: Any, /) -> Any: ...

    def __ge__(self, other: Any, /) -> Any:
        """Checks if the set is a superset of given one."""
        return (
            len(self) >= len(other) and all(value in self for value in other)
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    @overload
    def __gt__(self, other: Self, /) -> bool: ...

    @overload
    def __gt__(self, other: Any, /) -> Any: ...

    def __gt__(self, other: Any, /) -> Any:
        """Checks if the set is a strict superset of given one."""
        return (
            len(self) > len(other) and self >= other and self != other
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    @overload
    def __le__(self, other: Self, /) -> bool: ...

    @overload
    def __le__(self, other: Any, /) -> Any: ...

    def __le__(self, other: Any, /) -> Any:
        """Checks if the set is a subset of given one."""
        return (
            len(self) <= len(other) and all(value in other for value in self)
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    @overload
    def __lt__(self, other: Self, /) -> bool: ...

    @overload
    def __lt__(self, other: Any, /) -> Any: ...

    def __lt__(self, other: Any, /) -> Any:
        """Checks if the set is a strict subset of given one."""
        return (
            len(self) < len(other) and self <= other and self != other
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    def __or__(self, other: AbstractSet[ValueT], /) -> Self:
        """Returns union of the set with given one."""
        return (
            self.from_iterable(chain(self, other))
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    def __sub__(self, other: AbstractSet[ValueT], /) -> Self:
        """Returns subtraction of the set with given one."""
        return (
            self.from_iterable(value for value in self if value not in other)
            if isinstance(other, AbstractSet)
            else NotImplemented
        )

    def __xor__(self, other: AbstractSet[ValueT], /) -> Self:
        """Returns symmetric difference of the set with given one."""
        return (
            (self - other) | (other - self)
            if isinstance(other, AbstractSet)
            else NotImplemented
        )


class MutableSet(AbstractSet[ValueT]):
    @abstractmethod
    def add(self, value: ValueT, /) -> None:
        """Adds given value to the set."""
        raise NotImplementedError

    @abstractmethod
    def clear(self, /) -> None:
        """Adds given value to the set."""
        raise NotImplementedError

    @abstractmethod
    def discard(self, value: ValueT, /) -> None:
        """Removes given value from the set if it is present."""
        raise NotImplementedError

    @abstractmethod
    def remove(self, value: ValueT, /) -> None:
        """Removes given value that is present in the set."""
        raise NotImplementedError

    __slots__ = ()

    def __iand__(self, other: AbstractSet[ValueT], /) -> Self:
        """Intersects the set with given one in-place."""
        if not isinstance(other, AbstractSet):
            return NotImplemented
        for value in self - other:
            self.discard(value)
        return self

    def __ior__(self, other: AbstractSet[ValueT], /) -> Self:
        """Unites the set with given one in-place."""
        if not isinstance(other, AbstractSet):
            return NotImplemented
        for value in other:
            self.add(value)
        return self

    def __isub__(self, other: AbstractSet[ValueT], /) -> Self:
        """Subtracts from the set a given one in-place."""
        if not isinstance(other, AbstractSet):
            return NotImplemented
        if self == other:
            self.clear()
        else:
            for value in other:
                self.discard(value)
        return self

    def __ixor__(self, other: AbstractSet[ValueT], /) -> Self:
        """Exclusively disjoins the set with given one in-place."""
        if not isinstance(other, AbstractSet):
            return NotImplemented
        if self == other:
            self.clear()
        else:
            for value in other:
                if value in self:
                    self.discard(value)
                else:
                    self.add(value)
        return self


class TreeWrapper(Protocol[KeyT, ValueT]):
    @property
    @abstractmethod
    def _tree(self, /) -> Tree[KeyT, ValueT]:
        raise NotImplementedError

    __slots__ = ()
