import weakref
from collections import deque
from collections.abc import Iterable, Sequence
from itertools import count, groupby
from typing import Any, Self, overload

from .hints import Item, KeyT, ValueT
from .nil import NIL, Nil


class AntisymmetricKeyIndex:
    __slots__ = 'index', 'key'

    def __init__(self, key_index: tuple[KeyT, int], /) -> None:
        self.key, self.index = key_index

    @overload
    def __eq__(self, other: Self, /) -> bool: ...

    @overload
    def __eq__(self, other: Any, /) -> Any: ...

    def __eq__(self, other: Any, /) -> Any:
        return (
            are_keys_equal(self.key, other.key)
            if isinstance(other, AntisymmetricKeyIndex)
            else NotImplemented
        )


def are_keys_equal(left: KeyT, right: KeyT, /) -> bool:
    return not (left < right or right < left)


def capacity(iterable: Iterable[Any], /) -> int:
    """
    Returns number of elements in iterable.

    >>> capacity(range(0))
    0
    >>> capacity(range(10))
    10
    """
    counter = count()
    # order matters: if `counter` goes first,
    # then it will be incremented even for empty `iterable`
    deque(zip(iterable, counter, strict=False), maxlen=0)
    return next(counter)


def to_balanced_tree_height(size: int, /) -> int:
    return size.bit_length() - 1


def dereference_maybe(
    maybe_reference: weakref.ref[ValueT] | Nil, /
) -> ValueT | Nil:
    if maybe_reference is not NIL:
        result = maybe_reference()
        assert result is not None
        return result
    return maybe_reference


def maybe_weakref(
    object_: ValueT | Nil, /
) -> weakref.ReferenceType[ValueT] | Nil:
    return object_ if object_ is NIL else weakref.ref(object_)


def to_unique_sorted_items(
    keys: Sequence[KeyT], values: Sequence[ValueT], /
) -> Sequence[Item[Any, ValueT]]:
    return [
        (index_key.key, values[-index_key.index])
        for index_key, _ in groupby(
            sorted([(key, -index) for index, key in enumerate(keys)]),
            key=AntisymmetricKeyIndex,
        )
    ]


def to_unique_sorted_values(values: list[ValueT], /) -> list[ValueT]:
    values.sort()
    return [value for value, _ in groupby(values)]


def split_items(
    items: Sequence[tuple[KeyT, ValueT]], /
) -> tuple[Sequence[KeyT], Sequence[ValueT]]:
    keys, values = tuple(zip(*items, strict=False)) if items else ((), ())
    return keys, values
