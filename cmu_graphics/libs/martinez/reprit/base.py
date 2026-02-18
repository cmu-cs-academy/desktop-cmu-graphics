from collections import (OrderedDict,
                         abc)
from inspect import (_ParameterKind,
                     signature as _signature)
from types import MethodType as _MethodType
from typing import (Any as _Any,
                    Callable as _Callable,
                    Iterable as _Iterable,
                    Union as _Union)

from . import (seekers as _seekers,
               serializers as _serializers)
from .core.hints import (Constructor as _Constructor,
                         Initializer as _Initializer)
from .hints import (ArgumentSerializer as _ArgumentSerializer,
                    FieldSeeker as _FieldSeeker)


def generate_repr(method: _Union[_Constructor, _Initializer],
                  *,
                  argument_serializer: _ArgumentSerializer
                  = _serializers.simple,
                  field_seeker: _FieldSeeker = _seekers.simple,
                  prefer_keyword: bool = False,
                  skip_defaults: bool = False,
                  with_module_name: bool = False) -> _Callable[[_Any], str]:
    """
    Generates ``__repr__`` method based on constructor/initializer parameters.

    We are assuming that no parameters data
    get thrown away during instance creation,
    so we can re-create it after.

    :param method:
        constructor/initializer method
        which parameters will be used in resulting representation.
    :param argument_serializer: function that serializes argument to string.
    :param field_seeker:
        function that re-creates parameter value
        based on class instance and name.
    :param prefer_keyword:
        flag that specifies
        if positional-or-keyword parameters should be outputted
        as keyword ones when possible.
    :param skip_defaults:
        flag that specifies
        if optional parameters with default arguments should be skipped.
    :param with_module_name:
        flag that specifies if module name should be added.

    >>> from reprit.base import generate_repr
    >>> class Person:
    ...     def __init__(self, name, *, address=None):
    ...         self.name = name
    ...         self.address = address
    ...     __repr__ = generate_repr(__init__,
    ...                              skip_defaults=True)
    >>> Person('Adrian')
    Person('Adrian')
    >>> Person('Mary', address='Somewhere on Earth')
    Person('Mary', address='Somewhere on Earth')
    >>> class ScoreBoard:
    ...     def __init__(self, first, *rest):
    ...         self.first = first
    ...         self.rest = rest
    ...     __repr__ = generate_repr(__init__,
    ...                              prefer_keyword=True)
    >>> ScoreBoard(1)
    ScoreBoard(first=1)
    >>> ScoreBoard(1, 40)
    ScoreBoard(1, 40)
    >>> class Student:
    ...     def __init__(self, name, group):
    ...         self.name = name
    ...         self.group = group
    ...     __repr__ = generate_repr(__init__,
    ...                              with_module_name=True)
    >>> Student('Kira', 132)
    reprit.base.Student('Kira', 132)
    >>> Student('Naomi', 248)
    reprit.base.Student('Naomi', 248)
    >>> from reprit import seekers
    >>> class Account:
    ...     def __init__(self, id_, *, balance=0):
    ...         self.id = id_
    ...         self.balance = balance
    ...     __repr__ = generate_repr(__init__,
    ...                              field_seeker=seekers.complex_)
    >>> Account(1)
    Account(1, balance=0)
    >>> Account(100, balance=-10)
    Account(100, balance=-10)
    >>> import json
    >>> class Object:
    ...     def __init__(self, value):
    ...         self.value = value
    ...     def serialized(self):
    ...         return json.dumps(self.value)
    ...     @classmethod
    ...     def from_serialized(cls, serialized):
    ...         return cls(json.loads(serialized))
    ...     __repr__ = generate_repr(from_serialized)
    >>> Object.from_serialized('0')
    Object.from_serialized('0')
    >>> Object.from_serialized('{"key": "value"}')
    Object.from_serialized('{"key": "value"}')
    """
    if with_module_name:
        def to_class_name(cls: type) -> str:
            return cls.__module__ + '.' + cls.__qualname__
    else:
        def to_class_name(cls: type) -> str:
            return cls.__qualname__

    unwrapped_method = (method.__func__
                        if isinstance(method, (classmethod, staticmethod))
                        else method)
    method_name = unwrapped_method.__name__
    parameters = OrderedDict(_signature(unwrapped_method).parameters)

    if method_name == '__init__' or method_name == '__new__':
        # remove `cls`/`self`
        parameters.popitem(False)

        def __repr__(self: _Any) -> str:
            return (to_class_name(type(self))
                    + '(' + ', '.join(to_arguments_strings(self)) + ')')
    else:
        if isinstance(method, classmethod):
            # remove `cls`
            parameters.popitem(False)

        def __repr__(self: _Any) -> str:
            return (to_class_name(type(self)) + '.' + method_name
                    + '(' + ', '.join(to_arguments_strings(self)) + ')')

    variadic_positional = next(
            (parameter
             for parameter in parameters.values()
             if parameter.kind is _ParameterKind.VAR_POSITIONAL),
            None)
    to_keyword_string = '{}={}'.format
    positional_only_parameters = [
        parameter
        for parameter in parameters.values()
        if parameter.kind is _ParameterKind.POSITIONAL_ONLY
    ]

    def to_arguments_strings(object_: _Any) -> _Iterable[str]:
        variadic_positional_unset = (
                variadic_positional is None
                or not field_seeker(object_, variadic_positional.name))
        positional_or_keyword_is_keyword = (prefer_keyword
                                            and variadic_positional_unset)
        fields = [seek_field(object_, name) for name in parameters.keys()]
        for index, (parameter, field) in enumerate(zip(parameters.values(),
                                                       fields)):
            kind = parameter.kind
            show_parameter = (
                    not skip_defaults
                    or field is not parameter.default
                    or (kind is _ParameterKind.POSITIONAL_OR_KEYWORD
                        and not variadic_positional_unset)
                    or (kind is _ParameterKind.POSITIONAL_ONLY
                        and
                        (not variadic_positional_unset
                         or any(field is not parameter.default
                                for parameter, field
                                in zip(positional_only_parameters[index + 1:],
                                       fields[index + 1:]))))
            )
            if show_parameter:
                if kind is _ParameterKind.POSITIONAL_ONLY:
                    yield argument_serializer(field)
                elif kind is _ParameterKind.POSITIONAL_OR_KEYWORD:
                    yield (to_keyword_string(parameter.name,
                                             argument_serializer(field))
                           if positional_or_keyword_is_keyword
                           else argument_serializer(field))
                elif kind is _ParameterKind.VAR_POSITIONAL:
                    yield from ((argument_serializer(field),)
                                # we don't want to exhaust iterator
                                if isinstance(field, abc.Iterator)
                                else map(argument_serializer, field))
                elif kind is _ParameterKind.KEYWORD_ONLY:
                    yield to_keyword_string(parameter.name,
                                            argument_serializer(field))
                else:
                    yield from map(to_keyword_string, field.keys(),
                                   map(argument_serializer, field.values()))
            elif (not positional_or_keyword_is_keyword
                  and (kind is _ParameterKind.POSITIONAL_ONLY
                       or kind is _ParameterKind.POSITIONAL_OR_KEYWORD)):
                positional_or_keyword_is_keyword = True

    def seek_field(object_: _Any, name: str) -> _Any:
        result = field_seeker(object_, name)
        if isinstance(result, _MethodType) and result.__self__ is object_:
            result = result()
        return result

    return __repr__
