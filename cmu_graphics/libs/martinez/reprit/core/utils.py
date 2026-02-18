from collections import defaultdict
from typing import (Callable,
                    Iterable,
                    List,
                    Tuple,
                    TypeVar)

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')


def group_by(iterable: Iterable[_T0],
             *,
             key: Callable[[_T0], _T1]) -> Iterable[Tuple[_T1, List[_T0]]]:
    result = defaultdict(list)
    for element in iterable:
        result[key(element)].append(element)
    return result.items()
