from .hints import Scalar


class BoundingBox:
    __slots__ = '_x_min', '_y_min', '_x_max', '_y_max'

    def __init__(self, x_min: Scalar, y_min: Scalar,
                 x_max: Scalar, y_max: Scalar) -> None:
        self._x_min = x_min
        self._y_min = y_min
        self._x_max = x_max
        self._y_max = y_max

    @property
    def x_min(self) -> Scalar:
        return self._x_min

    @property
    def y_min(self) -> Scalar:
        return self._y_min

    @property
    def x_max(self) -> Scalar:
        return self._x_max

    @property
    def y_max(self) -> Scalar:
        return self._y_max

    def __eq__(self, other: 'BoundingBox') -> bool:
        return (self._x_min == other._x_min
                and self._y_min == other._y_min
                and self._x_max == other._x_max
                and self._y_max == other._y_max
                if isinstance(other, BoundingBox)
                else NotImplemented)

    def __add__(self, other: 'BoundingBox') -> 'BoundingBox':
        return BoundingBox(min(self._x_min, other._x_min),
                           min(self._y_min, other._y_min),
                           max(self._x_max, other._x_max),
                           max(self._y_max, other._y_max))
