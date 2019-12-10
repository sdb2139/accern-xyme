# Stubs for pandas.tests.reshape.merge.test_multi (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

def left() -> Any:
    ...

def right() -> Any:
    ...

def left_multi() -> Any:
    ...

def right_multi() -> Any:
    ...

def on_cols_multi() -> Any:
    ...

def idx_cols_multi() -> Any:
    ...


class TestMergeMulti:
    index: Any = ...
    to_join: Any = ...
    data: Any = ...
    def setup_method(self) -> None:
        ...

    def test_merge_on_multikey(self, left: Any, right: Any, join_type: Any) -> None:
        ...

    def test_left_join_multi_index(self, left: Any, right: Any, sort: Any) -> None:
        ...

    def test_merge_right_vs_left(self, left: Any, right: Any, sort: Any) -> None:
        ...

    def test_compress_group_combinations(self) -> None:
        ...

    def test_left_join_index_preserve_order(self) -> None:
        ...

    def test_left_join_index_multi_match_multiindex(self) -> None:
        ...

    def test_left_join_index_multi_match(self) -> None:
        ...

    def test_left_merge_na_buglet(self) -> None:
        ...

    def test_merge_na_keys(self) -> None:
        ...

    def test_merge_datetime_index(self, klass: Any) -> None:
        ...

    def test_join_multi_levels(self) -> None:
        ...

    def test_join_multi_levels2(self) -> None:
        ...


class TestJoinMultiMulti:
    def test_join_multi_multi(self, left_multi: Any, right_multi: Any, join_type: Any, on_cols_multi: Any, idx_cols_multi: Any) -> None:
        ...

    def test_join_multi_empty_frames(self, left_multi: Any, right_multi: Any, join_type: Any, on_cols_multi: Any, idx_cols_multi: Any) -> None:
        ...

    def test_merge_datetime_index(self, box: Any) -> None:
        ...

    def test_single_common_level(self) -> None:
        ...
