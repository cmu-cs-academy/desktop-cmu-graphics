from typing import (Any as _Any,
                    Callable as _Callable)

ArgumentSerializer = _Callable[[_Any], str]
FieldSeeker = _Callable[[_Any, str], _Any]
