# Stubs for pandas.tests.extension.arrow.test_bool (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,import-error

from typing import Any
from pandas.tests.extension import base


def dtype() -> Any:
    ...


def data() -> Any:
    ...


def data_missing() -> Any:
    ...


class BaseArrowTests:
    ...


class TestDtype(BaseArrowTests, base.BaseDtypeTests):
    def test_array_type_with_arg(self, data: Any, dtype: Any) -> None:
        ...


class TestInterface(BaseArrowTests, base.BaseInterfaceTests):
    def test_copy(self, data: Any) -> None:
        ...


class TestConstructors(BaseArrowTests, base.BaseConstructorsTests):
    def test_from_dtype(self, data: Any) -> None:
        ...

    def test_from_sequence_from_cls(self, data: Any) -> None:
        ...


class TestReduce(base.BaseNoReduceTests):
    def test_reduce_series_boolean(self) -> None:  #type: ignore
        ...


class TestReduceBoolean(base.BaseBooleanReduceTests):
    ...


def test_is_bool_dtype(data: Any) -> None:
    ...
