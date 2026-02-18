from functools import reduce
from operator import add
from typing import (Iterator,
                    List)

from .bounding_box import BoundingBox
from .contour import Contour


class Polygon:
    __slots__ = '_contours',

    def __init__(self, contours: List[Contour]) -> None:
        self._contours = contours

    @property
    def contours(self) -> List[Contour]:
        return self._contours

    def __eq__(self, other: 'Polygon') -> bool:
        return (self._contours == other._contours
                if isinstance(other, Polygon)
                else NotImplemented)

    def __iter__(self) -> Iterator[Contour]:
        return iter(self._contours)

    @property
    def bounding_box(self) -> BoundingBox:
        if self._contours:
            return reduce(add, [contour.bounding_box
                                for contour in self._contours])
        else:
            return BoundingBox(0, 0, 0, 0)

    def join(self, other: 'Polygon') -> None:
        contours_count = len(self._contours)
        self._contours.extend(Contour(contour.points,
                                      [hole + contours_count
                                       for hole in contour.holes],
                                      contour.is_external)
                              for contour in other._contours)
