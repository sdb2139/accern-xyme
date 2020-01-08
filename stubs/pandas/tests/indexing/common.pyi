# Stubs for pandas.tests.indexing.common (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=blacklisted-name

from typing import Any, Optional

class Base:
    series_ints: Any = ...
    frame_ints: Any = ...
    series_uints: Any = ...
    frame_uints: Any = ...
    series_floats: Any = ...
    frame_floats: Any = ...
    series_multi: Any = ...
    frame_multi: Any = ...
    series_labels: Any = ...
    frame_labels: Any = ...
    series_mixed: Any = ...
    frame_mixed: Any = ...
    series_ts: Any = ...
    frame_ts: Any = ...
    series_ts_rev: Any = ...
    frame_ts_rev: Any = ...
    frame_empty: Any = ...
    series_empty: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def generate_indices(self, f: Any, values: bool = ...) -> Any:
        ...

    def get_result(self, obj: Any, method: Any, key: Any, axis: Any) -> Any:
        ...

    def get_value(self, f: Any, i: Any, values: bool = ...) -> Any:
        ...

    def check_values(self, f: Any, func: Any, values: bool = ...) -> None:
        ...

    def check_result(self, name: Any, method1: Any, key1: Any, method2: Any, key2: Any, typs: Optional[Any] = ..., objs: Optional[Any] = ..., axes: Optional[Any] = ..., fails: Optional[Any] = ...) -> None:
        ...