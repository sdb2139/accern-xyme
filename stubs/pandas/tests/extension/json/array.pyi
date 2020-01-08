# Stubs for pandas.tests.extension.json.array (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any, Optional
from pandas.core.arrays import ExtensionArray
from pandas.core.dtypes.base import ExtensionDtype

class JSONDtype(ExtensionDtype):
    type: Any = ...
    name: str = ...
    na_value: Any = ...
    @classmethod
    def construct_array_type(cls):
        ...

    @classmethod
    def construct_from_string(cls, string: Any) -> Any:
        ...


class JSONArray(ExtensionArray):
    dtype: Any = ...
    __array_priority__: int = ...
    data: Any = ...
    def __init__(self, values: Any, dtype: Optional[Any] = ..., copy: bool = ...) -> None:
        ...

    def __getitem__(self, item: Any) -> Any:
        ...

    def __setitem__(self, key: Any, value: Any) -> None:
        ...

    def __len__(self):
        ...

    @property
    def nbytes(self):
        ...

    def isna(self):
        ...

    def take(self, indexer: Any, allow_fill: bool = ..., fill_value: Optional[Any] = ...) -> Any:
        ...

    def copy(self):
        ...

    def astype(self, dtype: Any, copy: bool = ...) -> Any:
        ...

    def unique(self) -> Any:
        ...


def make_data():
    ...