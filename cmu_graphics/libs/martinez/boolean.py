import enum
from copy import copy
from functools import partial
from operator import attrgetter
from typing import (Callable,
                    Dict,
                    List,
                    Optional,
                    Tuple,
                    TypeVar)

from .dendroid import red_black
from .prioq.base import PriorityQueue

from .contour import Contour
from .point import Point
from .polygon import Polygon
from .segment import Segment
from .utilities import (find_intersections,
                        sign,
                        to_segments)

Domain = TypeVar('Domain')


class _EnumBase(enum.IntEnum):
    def __repr__(self) -> str:
        return type(self).__qualname__ + '.' + self.name


@enum.unique
class EdgeType(_EnumBase):
    NORMAL = 0
    NON_CONTRIBUTING = 1
    SAME_TRANSITION = 2
    DIFFERENT_TRANSITION = 3


@enum.unique
class OperationType(_EnumBase):
    INTERSECTION = 0
    UNION = 1
    DIFFERENCE = 2
    XOR = 3


@enum.unique
class PolygonType(_EnumBase):
    SUBJECT = 0
    CLIPPING = 1


def traverse(object_: Domain,
             left_links: Dict[int, int],
             right_links: Dict[int, int],
             to_left: Callable[[Domain], Optional[Domain]],
             to_right: Callable[[Domain], Optional[Domain]]) -> List[Domain]:
    registry = {}
    result = []
    queue = [object_]
    while queue:
        cursor = queue.pop()
        registry[id(cursor)] = len(result)
        result.append(cursor)
        left = to_left(cursor)
        if left is not None and id(left) not in registry:
            queue.append(left)
        right = to_right(cursor)
        if right is not None and id(right) not in registry:
            queue.append(right)
    queue = [object_]
    visited = {id(object_)}
    while queue:
        cursor = queue.pop()
        index = registry[id(cursor)]
        left = to_left(cursor)
        if left is not None:
            left_links[index] = registry[id(left)]
            if id(left) not in visited:
                visited.add(id(left))
                queue.append(left)
        right = to_right(cursor)
        if right is not None:
            right_links[index] = registry[id(right)]
            if id(right) not in visited:
                visited.add(id(right))
                queue.append(right)
    return result


PlainSweepEventState = Tuple[bool, Point, PolygonType, EdgeType,
                             bool, bool, bool, bool, int, int]
SweepEventState = Tuple[List[PlainSweepEventState],
                        Dict[int, int], Dict[int, int]]


class SweepEvent:
    __slots__ = ('is_left', 'point', 'other_event', 'polygon_type',
                 'edge_type', 'in_out', 'other_in_out', 'in_result',
                 'result_in_out', 'position', 'contour_id',
                 'prev_in_result_event')

    def __init__(self, is_left: bool, point: Point,
                 other_event: Optional['SweepEvent'],
                 polygon_type: PolygonType,
                 edge_type: EdgeType,
                 in_out: bool = False, other_in_out: bool = False,
                 in_result: bool = False,
                 result_in_out: bool = False,
                 position: int = 0,
                 contour_id: int = 0,
                 prev_in_result_event: Optional['SweepEvent'] = None) -> None:
        self.is_left = is_left
        self.point = point
        self.other_event = other_event
        self.polygon_type = polygon_type
        self.edge_type = edge_type
        self.in_out = in_out
        self.other_in_out = other_in_out
        self.in_result = in_result
        self.result_in_out = result_in_out
        self.position = position
        self.contour_id = contour_id
        self.prev_in_result_event = prev_in_result_event

    def __getstate__(self) -> SweepEventState:
        left_links, right_links = {}, {}
        events = self._traverse(self, left_links, right_links)
        return ([(event.is_left, event.point, event.polygon_type,
                  event.edge_type, event.in_out, event.other_in_out,
                  event.in_result, event.result_in_out,
                  event.position, event.contour_id)
                 for event in events],
                left_links, right_links)

    def __setstate__(self, state: SweepEventState) -> None:
        events_states, left_links, right_links = state
        (self.is_left, self.point, self.polygon_type, self.edge_type,
         self.in_out, self.other_in_out, self.in_result, self.result_in_out,
         self.position, self.contour_id) = events_states[0]
        self.other_event, self.prev_in_result_event = None, None
        events = [self] + [SweepEvent(event_state[0], event_state[1], None,
                                      event_state[2], event_state[3],
                                      event_state[4], event_state[5],
                                      event_state[6], event_state[7],
                                      event_state[8], event_state[9], None)
                           for event_state in events_states[1:]]
        for source, destination in left_links.items():
            events[source].other_event = events[destination]
        for source, destination in right_links.items():
            events[source].prev_in_result_event = events[destination]

    def __eq__(self, other: 'SweepEvent') -> bool:
        if self is other:
            return True

        def are_equal(left: SweepEvent, right: SweepEvent) -> bool:
            left_left_links, left_right_links = {}, {}
            right_left_links, right_right_links = {}, {}
            left_events = self._traverse(left, left_left_links,
                                         left_right_links)
            right_events = self._traverse(right, right_left_links,
                                          right_right_links)
            return (left_left_links == right_left_links
                    and left_right_links == right_right_links
                    and len(left_events) == len(right_events)
                    and all(map(are_fields_equal, left_events, right_events)))

        def are_fields_equal(left: SweepEvent, right: SweepEvent) -> bool:
            return (left.is_left is right.is_left
                    and left.point == right.point
                    and left.polygon_type is right.polygon_type
                    and left.edge_type is right.edge_type
                    and left.in_out is right.in_out
                    and left.other_in_out is right.other_in_out
                    and left.in_result is right.in_result
                    and left.result_in_out is right.result_in_out
                    and left.position == right.position
                    and left.contour_id == right.contour_id)

        return (are_equal(self, other)
                if isinstance(other, SweepEvent)
                else NotImplemented)

    _traverse = staticmethod(
            partial(traverse,
                    to_left=attrgetter('other_event'),
                    to_right=attrgetter('prev_in_result_event')))

    @property
    def is_vertical(self) -> bool:
        self.validate()
        return self.point.x == self.other_event.point.x

    @property
    def segment(self) -> Segment:
        self.validate()
        return Segment(self.point, self.other_event.point)

    def is_above(self, point: Point) -> bool:
        return not self.is_below(point)

    def is_below(self, point: Point) -> bool:
        self.validate()
        return (sign(self.point, self.other_event.point, point) == 1
                if self.is_left
                else sign(self.other_event.point, self.point, point) == 1)

    def validate(self) -> None:
        if self.other_event is None:
            raise ValueError('No "other_event" found.')


class EventsQueueKey:
    __slots__ = '_event',

    def __init__(self, event: SweepEvent) -> None:
        self._event = event
    
    @property
    def event(self) -> SweepEvent:
        return self._event

    def __eq__(self, other: 'EventsQueueKey') -> bool:
        return (self._event == other._event
                if isinstance(other, EventsQueueKey)
                else NotImplemented)

    def __lt__(self, other: 'EventsQueueKey') -> bool:
        if not isinstance(other, EventsQueueKey):
            return NotImplemented
        if self._event.point.x != other._event.point.x:
            # different x-coordinate,
            # the event with lower x-coordinate is processed first
            return self._event.point.x > other._event.point.x
        elif self._event.point.y != other._event.point.y:
            # different points, but same x-coordinate,
            # the event with lower y-coordinate is processed first
            return self._event.point.y > other._event.point.y
        elif self._event.is_left is not other._event.is_left:
            # same point, but one is a left endpoint
            # and the other a right endpoint,
            # the right endpoint is processed first
            return self._event.is_left
        # same point, both events are left endpoints
        # or both are right endpoints
        elif sign(self._event.point, self._event.other_event.point,
                  other._event.other_event.point):  # not collinear
            # the event associate to the bottom segment is processed first
            return self._event.is_above(other._event.other_event.point)
        else:
            return self._event.polygon_type > other._event.polygon_type


class SweepLineKey:
    __slots__ = '_event',

    def __init__(self, event: SweepEvent) -> None:
        self._event = event

    @property
    def event(self) -> SweepEvent:
        return self._event

    def __eq__(self, other: 'SweepLineKey') -> bool:
        return (self._event == other._event
                if isinstance(other, SweepLineKey)
                else NotImplemented)

    def __lt__(self, other: 'SweepLineKey') -> bool:
        if not isinstance(other, SweepLineKey):
            return NotImplemented
        if self is other:
            return False
        if not (sign(self.event.point, self.event.other_event.point,
                     other.event.point)
                or sign(self.event.point, self.event.other_event.point,
                        other.event.other_event.point)):
            # segments are collinear
            return (EventsQueueKey(self.event) < EventsQueueKey(other.event)
                    if self.event.polygon_type is other.event.polygon_type
                    else self.event.polygon_type < other.event.polygon_type)
        # segments are not collinear
        elif self.event.point == other.event.point:
            # same left endpoint, use the right endpoint to sort
            return self.event.is_below(other.event.other_event.point)
        # different left endpoint, use the left endpoint to sort
        elif self.event.point.x == other.event.point.x:
            return self.event.point.y < other.event.point.y
        elif EventsQueueKey(self.event) < EventsQueueKey(other.event):
            # has the line segment associated to `self` been inserted
            # into sweep line after the line segment associated to `other`?
            return other.event.is_above(self.event.point)
        else:
            # the line segment associated to `other` has been inserted
            # into sweep line after the line segment associated to `self`
            return self.event.is_below(other.event.point)


class Operation:
    __slots__ = ('_left', '_right', '_type', '_events_queue', '_resultant',
                 '_already_run')

    def __init__(self, left: Polygon, right: Polygon,
                 type_: OperationType) -> None:
        self._left = left
        self._right = right
        self._type = type_
        self._events_queue = PriorityQueue(key=EventsQueueKey,
                                           reverse=True)
        self._resultant = Polygon([])
        self._already_run = False

    def __eq__(self, other: 'Operation') -> bool:
        return (self._left == other._left
                and self._right == other._right
                and self._type is other._type
                if isinstance(other, Operation)
                else NotImplemented)

    @property
    def left(self) -> Polygon:
        return self._left

    @property
    def right(self) -> Polygon:
        return self._right

    @property
    def events(self) -> List[SweepEvent]:
        events_queue = copy(self._events_queue)
        return [events_queue.pop() for _ in range(len(events_queue))]

    @property
    def resultant(self) -> Polygon:
        return self._resultant

    @property
    def type(self) -> OperationType:
        return self._type

    @property
    def is_trivial(self) -> bool:
        # test 1 for trivial result case
        if not (self._left.contours and self._right.contours):
            # at least one of the polygons is empty
            if self._type is OperationType.DIFFERENCE:
                self._resultant = self._left
            if (self._type is OperationType.UNION
                    or self._type is OperationType.XOR):
                self._resultant = (self._left
                                   if self._left.contours
                                   else self._right)
            self._already_run = True
            return True
        # test 2 for trivial result case
        left_bounding_box = self._left.bounding_box
        right_bounding_box = self._right.bounding_box
        if (left_bounding_box.x_min > right_bounding_box.x_max
                or right_bounding_box.x_min > left_bounding_box.x_max
                or left_bounding_box.y_min > right_bounding_box.y_max
                or right_bounding_box.y_min > left_bounding_box.y_max):
            # the bounding boxes do not overlap
            if self._type is OperationType.DIFFERENCE:
                self._resultant = self._left
            elif (self._type is OperationType.UNION
                  or self._type is OperationType.XOR):
                self._resultant = self._left
                self._resultant.join(self._right)
            self._already_run = True
            return True
        return False

    @staticmethod
    def collect_events(events: List[SweepEvent]) -> List[SweepEvent]:
        result = [event
                  for event in events
                  if event.is_left and event.in_result
                  or not event.is_left and event.other_event.in_result]
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for index in range(len(result) - 1):
                if (EventsQueueKey(result[index])
                        < EventsQueueKey(result[index + 1])):
                    result[index], result[index + 1] = (result[index + 1],
                                                        result[index])
                    is_sorted = False
        for index, event in enumerate(result):
            event.position = index
            if not event.is_left:
                event.position, event.other_event.position = (
                    event.other_event.position, event.position)
        return result

    def connect_edges(self, events: List[SweepEvent]) -> None:
        self.process_events(self.collect_events(events))

    def divide_segment(self, event: SweepEvent, point: Point) -> None:
        # "left event" of the "right line segment"
        # resulting from dividing event.segment
        left_event = SweepEvent(True, point, event.other_event,
                                event.polygon_type,
                                EdgeType.NORMAL)
        # "right event" of the "left line segment"
        # resulting from dividing event.segment
        right_event = SweepEvent(False, point, event, event.polygon_type,
                                 EdgeType.NORMAL)
        if EventsQueueKey(left_event) < EventsQueueKey(event.other_event):
            # avoid a rounding error,
            # the left event would be processed after the right event
            event.other_event.is_left = True
            left_event.is_left = False
        event.other_event.other_event = left_event
        event.other_event = right_event
        self._events_queue.push(left_event)
        self._events_queue.push(right_event)

    def in_result(self, event: SweepEvent) -> bool:
        operation_type = self._type
        edge_type = event.edge_type
        if edge_type is EdgeType.NORMAL:
            if operation_type is OperationType.INTERSECTION:
                return not event.other_in_out
            elif operation_type is OperationType.UNION:
                return event.other_in_out
            elif operation_type is OperationType.DIFFERENCE:
                return (event.polygon_type is PolygonType.SUBJECT
                        and event.other_in_out
                        or event.polygon_type is PolygonType.CLIPPING
                        and not event.other_in_out)
            else:
                return operation_type is OperationType.XOR
        elif edge_type is EdgeType.SAME_TRANSITION:
            return (operation_type is OperationType.INTERSECTION
                    or operation_type is OperationType.UNION)
        elif edge_type is EdgeType.DIFFERENT_TRANSITION:
            return operation_type is OperationType.DIFFERENCE
        else:
            return False

    def possible_intersection(self,
                              first_event: SweepEvent,
                              second_event: SweepEvent) -> int:
        intersections_count, first_point, second_point = find_intersections(
                first_event.segment, second_event.segment)

        if not intersections_count:
            # no intersection
            return 0

        if ((intersections_count == 1) and
                (first_event.point == second_event.point or
                 (first_event.other_event.point
                  == second_event.other_event.point))):
            # the line segments intersect at an endpoint of both line segments
            return 0

        if (intersections_count == 2
                and first_event.polygon_type is second_event.polygon_type):
            raise ValueError("Edges of the same polygon should not overlap.")

        # The line segments associated to le1 and le2 intersect
        if intersections_count == 1:
            if (first_event.point != first_point
                    and first_event.other_event.point != first_point):
                # if the intersection point is not an endpoint of le1.segment
                self.divide_segment(first_event, first_point)
            if (second_event.point != first_point
                    and second_event.other_event.point != first_point):
                # if the intersection point is not an endpoint of le2.segment
                self.divide_segment(second_event, first_point)
            return 1

        # The line segments associated to le1 and le2 overlap
        sorted_events = []
        if first_event.point == second_event.point:
            sorted_events.append(None)
        elif EventsQueueKey(first_event) < EventsQueueKey(second_event):
            sorted_events.append(second_event)
            sorted_events.append(first_event)
        else:
            sorted_events.append(first_event)
            sorted_events.append(second_event)

        if first_event.other_event.point == second_event.other_event.point:
            sorted_events.append(None)
        elif (EventsQueueKey(first_event.other_event)
              < EventsQueueKey(second_event.other_event)):
            sorted_events.append(second_event.other_event)
            sorted_events.append(first_event.other_event)
        else:
            sorted_events.append(first_event.other_event)
            sorted_events.append(second_event.other_event)

        if (len(sorted_events) == 2
                or len(sorted_events) == 3 and sorted_events[2]):
            # both line segments are equal or share the left endpoint
            first_event.edge_type = EdgeType.NON_CONTRIBUTING
            second_event.edge_type = (
                EdgeType.SAME_TRANSITION
                if first_event.in_out is second_event.in_out
                else EdgeType.DIFFERENT_TRANSITION)
            if len(sorted_events) == 3:
                self.divide_segment(sorted_events[2].other_event,
                                    sorted_events[1].point)
            return 2
        if len(sorted_events) == 3:
            # the line segments share the right endpoint
            self.divide_segment(sorted_events[0], sorted_events[1].point)
            return 3

        if sorted_events[0] is not sorted_events[3].other_event:
            # no line segment includes totally the other one
            self.divide_segment(sorted_events[0], sorted_events[1].point)
            self.divide_segment(sorted_events[1], sorted_events[2].point)
            return 3

        # one line segment includes the other one
        self.divide_segment(sorted_events[0], sorted_events[1].point)
        self.divide_segment(sorted_events[3].other_event,
                            sorted_events[2].point)
        return 3

    def process_events(self, events: List[SweepEvent]) -> None:
        depth, hole_of = [], []
        processed = [False] * len(events)
        contours = self._resultant.contours
        for index, event in enumerate(events):
            if processed[index]:
                continue
            contour = Contour([], [], True)
            contour_id = len(contours)
            contours.append(contour)
            depth.append(0)
            hole_of.append(-1)
            if event.prev_in_result_event is not None:
                lower_contour_id = event.prev_in_result_event.contour_id
                if not event.prev_in_result_event.result_in_out:
                    contours[lower_contour_id].add_hole(contour_id)
                    hole_of[contour_id] = lower_contour_id
                    depth[contour_id] = depth[lower_contour_id] + 1
                    contour.is_external = False
                elif not contours[lower_contour_id].is_external:
                    contours[hole_of[lower_contour_id]].add_hole(contour_id)
                    hole_of[contour_id] = hole_of[lower_contour_id]
                    depth[contour_id] = depth[lower_contour_id]
                    contour.is_external = False
            position = index
            initial = event.point
            contour.add(initial)
            event = events[position]
            while event.other_event.point != initial:
                processed[position] = True
                if event.is_left:
                    event.result_in_out = False
                    event.contour_id = contour_id
                else:
                    event.other_event.result_in_out = True
                    event.other_event.contour_id = contour_id
                position = event.position
                processed[position] = True
                contour.add(events[position].point)
                position = self.to_next_position(position, events, processed)
                event = events[position]
            processed[position] = processed[event.position] = True
            event.other_event.result_in_out = True
            event.other_event.contour_id = contour_id
            if depth[contour_id] & 1:
                contour.reverse()

    def process_segments(self) -> None:
        for contour in self._left.contours:
            for segment in to_segments(contour.points):
                self._process_segment(segment, PolygonType.SUBJECT)
        for contour in self._right.contours:
            for segment in to_segments(contour.points):
                self._process_segment(segment, PolygonType.CLIPPING)

    def _process_segment(self, segment: Segment,
                         polygon_type: PolygonType) -> None:
        source_event = SweepEvent(True, segment.source, None, polygon_type,
                                  EdgeType.NORMAL)
        target_event = SweepEvent(True, segment.target, source_event,
                                  polygon_type, EdgeType.NORMAL)
        source_event.other_event = target_event
        if segment.min == segment.source:
            target_event.is_left = False
        else:
            source_event.is_left = False
        self._events_queue.push(source_event)
        self._events_queue.push(target_event)

    def sweep(self) -> List[SweepEvent]:
        min_max_x = min(self._left.bounding_box.x_max,
                        self._right.bounding_box.x_max)
        result = []
        events_queue = self._events_queue
        sweep_line = red_black.set_(key=SweepLineKey)
        while events_queue:
            event = events_queue.peek()
            if (self._type is OperationType.INTERSECTION
                    and event.point.x > min_max_x
                    or self._type is OperationType.DIFFERENCE
                    and event.point.x > self._left.bounding_box.x_max):
                break
            result.append(event)
            events_queue.pop()
            if event.is_left:
                sweep_line.add(event)
                try:
                    next_event = sweep_line.next(event)
                except ValueError:
                    next_event = None
                try:
                    previous_event = sweep_line.prev(event)
                except ValueError:
                    previous_event = None
                self.compute_fields(event, previous_event)
                if next_event is not None:
                    if self.possible_intersection(event, next_event) == 2:
                        self.compute_fields(event, previous_event)
                        self.compute_fields(next_event, event)
                if previous_event is not None:
                    if self.possible_intersection(previous_event, event) == 2:
                        try:
                            pre_previous_event = sweep_line.prev(
                                    previous_event)
                        except ValueError:
                            pre_previous_event = None
                        self.compute_fields(previous_event, pre_previous_event)
                        self.compute_fields(event, previous_event)
            else:
                event = event.other_event
                if event not in sweep_line:
                    continue
                try:
                    next_event = sweep_line.next(event)
                except ValueError:
                    next_event = None
                try:
                    previous_event = sweep_line.prev(event)
                except ValueError:
                    previous_event = None
                sweep_line.remove(event)
                if next_event is not None and previous_event is not None:
                    self.possible_intersection(previous_event, next_event)
        return result

    def compute_fields(self, event: SweepEvent,
                       previous_event: Optional[SweepEvent]) -> None:
        if previous_event is None:
            event.in_out = False
            event.other_in_out = True
        else:
            if event.polygon_type is previous_event.polygon_type:
                event.in_out = not previous_event.in_out
                event.other_in_out = previous_event.other_in_out
            else:
                event.in_out = not previous_event.other_in_out
                event.other_in_out = (not previous_event.in_out
                                      if previous_event.is_vertical
                                      else previous_event.in_out)
            event.prev_in_result_event = (
                previous_event.prev_in_result_event
                if (not self.in_result(previous_event)
                    or previous_event.is_vertical)
                else previous_event)
        event.in_result = self.in_result(event)

    def run(self) -> None:
        if self._already_run:
            return
        if self.is_trivial:
            return
        self.process_segments()
        self.connect_edges(self.sweep())
        self._already_run = True

    @staticmethod
    def to_next_position(position: int, events: List[SweepEvent],
                         processed: List[bool]) -> int:
        result = position + 1
        while (result < len(events)
               and events[result].point == events[position].point):
            if not processed[result]:
                return result
            else:
                result += 1
        if not position:
            return 0
        result = position - 1
        while processed[result]:
            if not result:
                break
            result -= 1
        return result


def compute(left: Polygon, right: Polygon,
            operation_type: OperationType) -> Polygon:
    operation = Operation(left, right, operation_type)
    operation.run()
    return operation.resultant
