# Stubs for pandas.core.indexes.accessors (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,too-many-ancestors

from typing import Any
from pandas.core.accessor import PandasDelegate
from pandas.core.base import NoNewAttributesMixin, PandasObject

class Properties(PandasDelegate, PandasObject, NoNewAttributesMixin):
    orig: Any = ...
    name: Any = ...
    def __init__(self, data: Any, orig: Any) -> None:
        ...


class DatetimeProperties(Properties):
    def to_pydatetime(self):
        ...

    @property
    def freq(self):
        ...


class TimedeltaProperties(Properties):
    def to_pytimedelta(self):
        ...

    @property
    def components(self):
        ...

    @property
    def freq(self):
        ...


class PeriodProperties(Properties):
    ...


class CombinedDatetimelikeProperties(DatetimeProperties, TimedeltaProperties, PeriodProperties):
    def __new__(cls, data: Any) -> Any:
        ...