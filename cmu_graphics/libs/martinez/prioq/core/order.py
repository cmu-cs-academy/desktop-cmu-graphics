from typing import Any, Generic, TypeVar, Self, overload

from cmu_graphics.libs.martinez.reprit.base import generate_repr

from .hints import HasCustomRepr, Ordered

_T = TypeVar('_T', bound=Ordered)


class NaturalOrder(HasCustomRepr, Generic[_T]):
    __slots__ = ('_value',)

    def __init__(self, _value: _T, /) -> None:
        self._value = _value

    __repr__ = generate_repr(__init__)

    @overload
    def __eq__(self, other: Self, /) -> bool: ...

    @overload
    def __eq__(self, other: Any, /) -> Any: ...

    def __eq__(self, other: Any, /) -> Any:
        return (
            self._value == other._value
            if isinstance(other, NaturalOrder)
            else NotImplemented
        )

    def __lt__(self, other: Self, /) -> bool:
        return self._value < other._value


class ReversedOrder(HasCustomRepr, Generic[_T]):
    __slots__ = ('_value',)

    def __init__(self, _value: _T, /) -> None:
        self._value = _value

    __repr__ = generate_repr(__init__)

    @overload
    def __eq__(self, other: Self, /) -> bool: ...

    @overload
    def __eq__(self, other: Any, /) -> Any: ...

    def __eq__(self, other: Any, /) -> Any:
        return (
            self._value == other._value
            if isinstance(other, ReversedOrder)
            else NotImplemented
        )

    def __lt__(self, other: Self, /) -> bool:
        return other._value < self._value
