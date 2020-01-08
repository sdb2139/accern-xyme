# Stubs for pandas.tests.reshape.merge.test_join (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

a_: Any

class TestJoin:
    df: Any = ...
    df2: Any = ...
    target: Any = ...
    source: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def test_cython_left_outer_join(self) -> None:
        ...

    def test_cython_right_outer_join(self) -> None:
        ...

    def test_cython_inner_join(self) -> None:
        ...

    def test_left_outer_join(self) -> None:
        ...

    def test_right_outer_join(self) -> None:
        ...

    def test_full_outer_join(self) -> None:
        ...

    def test_inner_join(self) -> None:
        ...

    def test_handle_overlap(self) -> None:
        ...

    def test_handle_overlap_arbitrary_key(self) -> None:
        ...

    def test_join_on(self) -> None:
        ...

    def test_join_on_fails_with_different_right_index(self) -> None:
        ...

    def test_join_on_fails_with_different_left_index(self) -> None:
        ...

    def test_join_on_fails_with_different_column_counts(self) -> None:
        ...

    def test_join_on_fails_with_wrong_object_type(self, wrong_type: Any) -> None:
        ...

    def test_join_on_pass_vector(self) -> None:
        ...

    def test_join_with_len0(self) -> None:
        ...

    def test_join_on_inner(self) -> None:
        ...

    def test_join_on_singlekey_list(self) -> None:
        ...

    def test_join_on_series(self) -> None:
        ...

    def test_join_on_series_buglet(self) -> None:
        ...

    def test_join_index_mixed(self, join_type: Any) -> None:
        ...

    def test_join_index_mixed_overlap(self) -> None:
        ...

    def test_join_empty_bug(self) -> None:
        ...

    def test_join_unconsolidated(self) -> None:
        ...

    def test_join_multiindex(self) -> None:
        ...

    def test_join_inner_multiindex(self) -> None:
        ...

    def test_join_hierarchical_mixed(self) -> None:
        ...

    def test_join_float64_float32(self) -> None:
        ...

    def test_join_many_non_unique_index(self) -> None:
        ...

    def test_join_sort(self) -> None:
        ...

    def test_join_mixed_non_unique_index(self) -> None:
        ...

    def test_join_non_unique_period_index(self) -> None:
        ...

    def test_mixed_type_join_with_suffix(self) -> None:
        ...

    def test_join_many(self) -> None:
        ...

    def test_join_many_mixed(self) -> None:
        ...

    def test_join_dups(self) -> None:
        ...

    def test_join_multi_to_multi(self, join_type: Any) -> None:
        ...

    def test_join_on_tz_aware_datetimeindex(self) -> None:
        ...