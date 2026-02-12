from __future__ import annotations

from typing import overload as _overload

from cmu_graphics.libs.martinez.dendroid._core.hints import (
    Item as _Item,
    KeyT as _KeyT,
    Order as _Order,
    ValueT as _ValueT,
)
from ._core.maps import Map as _Map
from ._core.red_black import Tree as _Tree
from ._core.sets import KeyedSet as _KeyedSet, Set as _Set
from ._core.utils import split_items as _split_items


def map_(*items: _Item[_KeyT, _ValueT]) -> _Map[_KeyT, _ValueT]:
    return _Map(_Tree.from_components(*_split_items(items)))


@_overload
def set_(*values: _ValueT, key: None = ...) -> _Set[_ValueT]: ...


@_overload
def set_(
    *values: _ValueT, key: _Order[_ValueT, _KeyT]
) -> _KeyedSet[_KeyT, _ValueT]: ...


def set_(
    *values: _ValueT, key: _Order[_ValueT, _KeyT] | None = None
) -> _KeyedSet[_KeyT, _ValueT] | _Set[_ValueT]:
    return (
        _Set(_Tree.from_components(values))
        if key is None
        else _KeyedSet(
            _Tree.from_components([key(value) for value in values], values),
            key,
        )
    )
