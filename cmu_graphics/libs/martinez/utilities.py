import math
from typing import (Optional,
                    Sequence,
                    Tuple)

from .hints import Scalar
from .point import Point
from .segment import Segment


def sign(first_point: Point, second_point: Point, third_point: Point) -> int:
    determinant = ((first_point.x - third_point.x)
                   * (second_point.y - third_point.y)
                   - (second_point.x - third_point.x)
                   * (first_point.y - third_point.y))
    if determinant > 0:
        return 1
    elif determinant < 0:
        return -1
    else:
        return 0


def _find_intersections(u0: Scalar, u1: Scalar, v0: Scalar, v1: Scalar
                        ) -> Tuple[int, Optional[Scalar], Optional[Scalar]]:
    first_coefficient = second_coefficient = None
    if u1 < v0 or u0 > v1:
        return 0, first_coefficient, second_coefficient
    if u1 > v0:
        if u0 < v1:
            first_coefficient = v0 if (u0 < v0) else u0
            second_coefficient = v1 if (u1 > v1) else u1
            return 2, first_coefficient, second_coefficient
        else:
            first_coefficient = u0
            return 1, first_coefficient, second_coefficient
    else:
        first_coefficient = u1
        return 1, first_coefficient, second_coefficient


def find_intersections(first_segment: Segment, second_segment: Segment,
                       *,
                       threshold: float = 1e-8,
                       squared_inv_epsilon: int = 10 ** 7
                       ) -> Tuple[int, Optional[Point], Optional[Point]]:
    first_source, second_source = first_segment.source, second_segment.source
    first_target, second_target = first_segment.target, second_segment.target
    first_vector = Point(first_target.x - first_source.x,
                         first_target.y - first_source.y)
    second_vector = Point(second_target.x - second_source.x,
                          second_target.y - second_source.y)
    e = Point(second_source.x - first_source.x,
              second_source.y - first_source.y)
    cross_product = (first_vector.x * second_vector.y
                     - first_vector.y * second_vector.x)
    squared_cross_product = cross_product * cross_product
    first_squared_length = (first_vector.x * first_vector.x
                            + first_vector.y * first_vector.y)
    second_squared_length = (second_vector.x * second_vector.x
                             + second_vector.y * second_vector.y)
    if squared_cross_product > (first_squared_length * second_squared_length
                                / squared_inv_epsilon):
        s = (e.x * second_vector.y - e.y * second_vector.x) / cross_product
        if (s < 0) or (s > 1):
            return 0, None, None
        t = (e.x * first_vector.y - e.y * first_vector.x) / cross_product
        if (t < 0) or (t > 1):
            return 0, None, None
        first_intersection_point = Point(first_source.x + s * first_vector.x,
                                         first_source.y + s * first_vector.y)
        if first_intersection_point.distance_to(first_source) < threshold:
            first_intersection_point = first_source
        elif first_intersection_point.distance_to(first_target) < threshold:
            first_intersection_point = first_target
        elif first_intersection_point.distance_to(second_source) < threshold:
            first_intersection_point = second_source
        elif first_intersection_point.distance_to(second_target) < threshold:
            first_intersection_point = second_target
        return 1, first_intersection_point, None
    e_squared_length = e.x * e.x + e.y * e.y
    cross_product = e.x * first_vector.y - e.y * first_vector.x
    squared_cross_product = cross_product * cross_product
    if squared_cross_product > (first_squared_length * e_squared_length
                                / squared_inv_epsilon):
        return 0, None, None
    s0 = first_vector.x * e.x + first_vector.y * e.y
    try:
        s0 /= first_squared_length
    except ArithmeticError:
        s0 = s1 = math.nan
    else:
        s1 = s0 + (first_vector.x * second_vector.x
                   + first_vector.y * second_vector.y) / first_squared_length
    s_min, s_max = min(s0, s1), max(s0, s1)
    (intersections_count, first_coefficient,
     second_coefficient) = _find_intersections(0, 1, s_min, s_max)
    first_intersection_point = second_intersection_point = None
    if intersections_count:
        first_intersection_point = Point(first_source.x
                                         + first_coefficient * first_vector.x,
                                         first_source.y
                                         + first_coefficient * first_vector.y)
        if first_intersection_point.distance_to(first_source) < threshold:
            first_intersection_point = first_source
        elif first_intersection_point.distance_to(first_target) < threshold:
            first_intersection_point = first_target
        elif first_intersection_point.distance_to(second_source) < threshold:
            first_intersection_point = second_source
        elif first_intersection_point.distance_to(second_target) < threshold:
            first_intersection_point = second_target
        if intersections_count > 1:
            second_intersection_point = Point(first_source.x
                                              + second_coefficient
                                              * first_vector.x,
                                              first_source.y
                                              + second_coefficient
                                              * first_vector.y)
    return (intersections_count, first_intersection_point,
            second_intersection_point)


def to_segments(vertices: Sequence[Point]) -> Sequence[Segment]:
    return [Segment(vertices[index], vertices[(index + 1) % len(vertices)])
            for index in range(len(vertices))]
