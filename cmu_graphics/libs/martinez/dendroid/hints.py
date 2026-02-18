from typing import TypeAlias as _TypeAlias

from ._core import hints as _hints, maps as _maps, sets as _sets
from ._core.hints import KeyT as _KeyT, ValueT as _ValueT

Item: _TypeAlias = _hints.Item[_KeyT, _ValueT]
Map: _TypeAlias = _maps.Map[_KeyT, _ValueT]
Order: _TypeAlias = _hints.Order[_ValueT, _KeyT]
KeyedSet: _TypeAlias = _sets.KeyedSet[_KeyT, _ValueT]
Set: _TypeAlias = _sets.Set[_ValueT]
