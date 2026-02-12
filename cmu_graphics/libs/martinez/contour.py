from functools import reduce
from operator import add
from typing import (Iterator,
                    List)
from .bounding_box import BoundingBox
from .point import Point


class Contour:
    __slots__ = '_points', '_holes', 'is_external'

    def __init__(self, points: List[Point], holes: List[int], is_external: bool
                 ) -> None:
        self._points = points
        self._holes = holes
        self.is_external = is_external

    def __iter__(self) -> Iterator[Point]:
        return iter(self._points)

    @property
    def points(self) -> List[Point]:
        return self._points

    @property
    def holes(self) -> List[int]:
        return self._holes

    @property
    def is_counterclockwise(self) -> bool:
        points = self._points
        signed_area = sum(
                points[index].x * points[(index + 1) % len(points)].y
                - points[(index + 1) % len(points)].x * points[index].y
                for index in range(len(points)))
        return signed_area >= 0

    @property
    def is_clockwise(self) -> bool:
        return not self.is_counterclockwise

    @property
    def bounding_box(self) -> BoundingBox:
        if self._points:
            return reduce(add, [point.bounding_box for point in self._points])
        else:
            return BoundingBox(0, 0, 0, 0)

    def __eq__(self, other: 'Contour') -> bool:
        return (self._points == other._points
                and self._holes == other._holes
                and self.is_external is other.is_external
                if isinstance(other, Contour)
                else NotImplemented)

    def add(self, point: Point) -> None:
        self._points.append(point)

    def add_hole(self, hole: int) -> None:
        self._holes.append(hole)

    def clear_holes(self) -> None:
        self._holes.clear()

    def reverse(self) -> None:
        self._points = self._points[::-1]

    def set_clockwise(self) -> None:
        if self.is_counterclockwise:
            self.reverse()

    def set_counterclockwise(self) -> None:
        if self.is_clockwise:
            self.reverse()
