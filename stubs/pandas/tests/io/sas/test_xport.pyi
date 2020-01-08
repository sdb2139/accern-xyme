# Stubs for pandas.tests.io.sas.test_xport (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

def numeric_as_float(data: Any) -> None:
    ...


class TestXport:
    dirpath: Any = ...
    file01: Any = ...
    file02: Any = ...
    file03: Any = ...
    file04: Any = ...
    def setup_method(self, datapath: Any) -> None:
        ...

    def test1_basic(self) -> None:
        ...

    def test1_index(self) -> None:
        ...

    def test1_incremental(self) -> None:
        ...

    def test2(self) -> None:
        ...

    def test_multiple_types(self) -> None:
        ...

    def test_truncated_float_support(self) -> None:
        ...