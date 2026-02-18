import sys as _sys
import typing as _t
from enum import Enum as _Enum
from functools import singledispatch as _singledispatch
from types import (BuiltinFunctionType as _BuiltinFunctionType,
                   BuiltinMethodType as _BuiltinMethodType,
                   ClassMethodDescriptorType as _ClassMethodDescriptorType,
                   FunctionType as _FunctionType,
                   GetSetDescriptorType as _GetSetDescriptorType,
                   MemberDescriptorType as _MemberDescriptorType,
                   MethodDescriptorType as _MethodDescriptorType,
                   MethodType as _MethodType,
                   MethodWrapperType as _MethodWrapperType,
                   ModuleType as _ModuleType,
                   WrapperDescriptorType as _WrapperDescriptorType)

_Params = _t.ParamSpec('_Params')
_T1 = _t.TypeVar('_T1')
_T2 = _t.TypeVar('_T2')


def _decorate_if(
        decorator: _t.Callable[[_t.Callable[_Params, _T1]], _t.Any],
        condition: bool
) -> _t.Callable[[_t.Callable[_Params, _T1]], _t.Any]:
    return decorator if condition else _identity_decorator


def _identity_decorator(
        value: _t.Callable[_Params, _T1]
) -> _t.Callable[_Params, _T1]:
    return value


simple = repr


@_singledispatch
def complex_(object_):
    return repr(object_)


@complex_.register(_BuiltinFunctionType)
@complex_.register(_FunctionType)
@complex_.register(type)
def _(object_: _t.Union[_BuiltinFunctionType, _FunctionType, type]) -> str:
    return object_.__module__ + '.' + object_.__qualname__


@_decorate_if(complex_.register(_BuiltinMethodType),
              _sys.implementation.name != 'pypy')
@complex_.register(_MethodType)
def _(object_: _t.Union[_BuiltinMethodType, _MethodType]) -> str:
    return complex_(object_.__self__) + '.' + object_.__name__


@_decorate_if(complex_.register(_ClassMethodDescriptorType),
              _sys.implementation.name != 'pypy')
@_decorate_if(complex_.register(_MethodDescriptorType),
              _sys.implementation.name != 'pypy')
@_decorate_if(complex_.register(_MethodWrapperType),
              _sys.implementation.name != 'pypy')
@_decorate_if(complex_.register(_WrapperDescriptorType),
              _sys.implementation.name != 'pypy')
@complex_.register(_GetSetDescriptorType)
@complex_.register(_MemberDescriptorType)
def _(
        object_: _t.Union[
            _ClassMethodDescriptorType, _GetSetDescriptorType,
            _MemberDescriptorType, _MethodDescriptorType, _MethodWrapperType,
            _WrapperDescriptorType
        ]
) -> str:
    return complex_(object_.__objclass__) + '.' + object_.__name__


@complex_.register(_Enum)
def _(object_: _Enum) -> str:
    return complex_(type(object_)) + '.' + object_.name


@complex_.register(_ModuleType)
def _(object_: _ModuleType) -> str:
    return object_.__name__


@complex_.register(classmethod)
@complex_.register(staticmethod)
def _(object_: _t.Union[classmethod, staticmethod]) -> str:
    return '{}({})'.format(complex_(type(object_)), complex_(object_.__func__))


@complex_.register(dict)
def _(object_: dict) -> str:
    return '{' + ', '.join(map('{}: {}'.format,
                               map(complex_, object_.keys()),
                               map(complex_, object_.values()))) + '}'


@complex_.register(frozenset)
def _(object_: frozenset) -> str:
    return (complex_(type(object_)) + '('
            + ('{' + ', '.join(map(complex_, object_)) + '}'
               if object_
               else '')
            + ')')


@complex_.register(list)
def _(object_: list) -> str:
    return '[' + ', '.join(map(complex_, object_)) + ']'


@complex_.register(memoryview)
def _(object_: memoryview) -> str:
    return complex_(type(object_)) + '(' + complex_(object_.obj) + ')'


@complex_.register(set)
def _(object_: set) -> str:
    return ('{' + ', '.join(map(complex_, object_)) + '}'
            if object_
            else complex_(type(object_)) + '()')


@complex_.register(tuple)
def _(object_: tuple) -> str:
    return ('(' + ', '.join(map(complex_, object_))
            + (',' if len(object_) == 1 else '') + ')')
