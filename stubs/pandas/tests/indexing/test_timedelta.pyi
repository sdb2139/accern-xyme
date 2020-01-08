# Stubs for pandas.tests.indexing.test_timedelta (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,too-many-ancestors

from typing import Any

class TestTimedeltaIndexing:
    def test_boolean_indexing(self) -> None:
        ...

    def test_list_like_indexing(self, indexer: Any, expected: Any) -> None:
        ...

    def test_string_indexing(self) -> None:
        ...

    def test_masked_setitem(self, value: Any) -> None:
        ...

    def test_listlike_setitem(self, value: Any) -> None:
        ...

    def test_numpy_timedelta_scalar_indexing(self, start: Any, stop: Any, expected_slice: Any) -> None:
        ...

    def test_roundtrip_thru_setitem(self) -> None:
        ...

    def test_loc_str_slicing(self) -> None:
        ...

    def test_loc_slicing(self) -> None:
        ...