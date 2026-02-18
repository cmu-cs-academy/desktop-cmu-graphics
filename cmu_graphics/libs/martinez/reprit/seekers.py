from typing import Any as _Any

from .core.utils import group_by as _group_by

simple = getattr


# handles names clash with built-ins
# (e.g. parameter ``id_`` and field ``id``)
# and "private" attributes
# (those with leading single-underscore,
# e.g. parameter ``value`` and field ``_value``,
# do not confuse with "mangled" ones, ``__value`` in our case)
# and both
# (like in case with parameter ``id_`` and field ``_id``)
def complex_(object_: _Any, parameter_name: str) -> _Any:
    try:
        return getattr(object_, parameter_name)
    except AttributeError as original_error:
        def is_candidate(name: str) -> bool:
            return parameter_name.strip('_') == name.strip('_')

        def grouping_key(name: str) -> int:
            return abs(len(name) - len(parameter_name))

        candidates = filter(is_candidate, dir(object_))
        key, group = min(_group_by(candidates,
                                   key=grouping_key))
        try:
            field_name, = group
        except ValueError:
            error = ValueError('Found {count} conflicting candidate fields '
                               'for parameter "{parameter}": "{candidates}".'
                               .format(count=len(group),
                                       parameter=parameter_name,
                                       candidates='", "'.join(group)))
            raise original_error from error
        return getattr(object_, field_name)
