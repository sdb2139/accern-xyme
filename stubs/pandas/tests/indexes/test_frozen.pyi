# Stubs for pandas.tests.indexes.test_frozen (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any
from pandas.tests.test_base import CheckImmutable, CheckStringMixin


class TestFrozenList(CheckImmutable, CheckStringMixin):
    mutable_methods: Any = ...
    unicode_container: Any = ...
    lst: Any = ...
    container: Any = ...
    klass: Any = ...

    def setup_method(self, _: Any) -> None:
        ...

    def test_add(self) -> None:
        ...

    def test_iadd(self) -> None:
        ...

    def test_union(self) -> None:
        ...

    def test_difference(self) -> None:
        ...

    def test_difference_dupe(self) -> None:
        ...

    def test_tricky_container_to_bytes_raises(self) -> None:
        ...


class TestFrozenNDArray(CheckImmutable, CheckStringMixin):
    mutable_methods: Any = ...
    lst: Any = ...
    klass: Any = ...
    container: Any = ...
    unicode_container: Any = ...

    def setup_method(self, _: Any) -> None:
        ...

    def test_constructor_warns(self) -> None:
        ...

    def test_tricky_container_to_bytes(self) -> None:
        ...

    def test_shallow_copying(self) -> None:
        ...

    def test_values(self) -> None:
        ...

    def test_searchsorted(self) -> None:
        ...
