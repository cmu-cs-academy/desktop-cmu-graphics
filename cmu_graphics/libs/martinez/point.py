import math

from .bounding_box import BoundingBox
from .hints import Scalar


class Point:
    __slots__ = '_x', '_y'

    def __init__(self, x: Scalar, y: Scalar) -> None:
        self._x = x
        self._y = y

    def __eq__(self, other: 'Point') -> bool:
        return (self._x == other._x and self._y == other._y
                if isinstance(other, Point)
                else NotImplemented)

    @property
    def bounding_box(self) -> BoundingBox:
        return BoundingBox(self._x, self._y, self._x, self._y)

    @property
    def x(self) -> Scalar:
        return self._x

    @property
    def y(self) -> Scalar:
        return self._y

    def distance_to(self, other: 'Point') -> Scalar:
        return math.sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)
