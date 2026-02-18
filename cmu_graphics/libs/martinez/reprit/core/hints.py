from typing import (Any,
                    Callable,
                    Union)

Constructor = Union[Callable[..., Any], classmethod, staticmethod]
Initializer = Callable[..., None]
