# Stubs for pandas.tests.window.test_pairwise (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any


class TestPairwise:
    df1s: Any = ...
    df2: Any = ...
    s: Any = ...

    def compare(self, result: Any, expected: Any) -> None:
        ...

    def test_no_flex(self, f: Any) -> None:
        ...

    def test_pairwise_with_self(self, f: Any) -> None:
        ...

    def test_no_pairwise_with_self(self, f: Any) -> None:
        ...

    def test_pairwise_with_other(self, f: Any) -> None:
        ...

    def test_no_pairwise_with_other(self, f: Any) -> None:
        ...

    def test_pairwise_with_series(self, f: Any) -> None:
        ...
