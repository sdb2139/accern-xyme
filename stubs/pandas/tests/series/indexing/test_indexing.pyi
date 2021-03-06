# Stubs for pandas.tests.series.indexing.test_indexing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

def test_basic_indexing() -> None:
    ...


def test_basic_getitem_with_labels(test_data: Any) -> None:
    ...


def test_getitem_setitem_ellipsis() -> None:
    ...


def test_getitem_get(test_data: Any) -> None:
    ...


def test_getitem_fancy(test_data: Any) -> None:
    ...


def test_getitem_generator(test_data: Any) -> None:
    ...


def test_type_promotion() -> None:
    ...


def test_getitem_with_duplicates_indices(result_1: Any, duplicate_item: Any, expected_1: Any) -> None:
    ...


def test_getitem_out_of_bounds(test_data: Any) -> None:
    ...


def test_getitem_setitem_integers() -> None:
    ...


def test_getitem_box_float64(test_data: Any) -> None:
    ...


def test_get(arr: Any) -> None:
    ...


def test_series_box_timestamp() -> None:
    ...


def test_getitem_ambiguous_keyerror() -> None:
    ...


def test_getitem_unordered_dup() -> None:
    ...


def test_getitem_dups_with_missing() -> None:
    ...


def test_getitem_dups() -> None:
    ...


def test_setitem_ambiguous_keyerror() -> None:
    ...


def test_getitem_dataframe() -> None:
    ...


def test_setitem(test_data: Any) -> None:
    ...


def test_setitem_dtypes() -> None:
    ...


def test_set_value(test_data: Any) -> None:
    ...


def test_setslice(test_data: Any) -> None:
    ...


def test_basic_getitem_setitem_corner(test_data: Any) -> None:
    ...


def test_setitem_with_tz(tz: Any) -> None:
    ...


def test_setitem_with_tz_dst() -> None:
    ...


def test_categorical_assigning_ops() -> None:
    ...


def test_slice(test_data: Any) -> None:
    ...


def test_slice_can_reorder_not_uniquely_indexed() -> None:
    ...


def test_loc_setitem(test_data: Any) -> None:
    ...


def test_setitem_na() -> None:
    ...


def test_timedelta_assignment() -> None:
    ...


def test_td64_series_assign_nat(nat_val: Any, should_cast: Any) -> None:
    ...


def test_append_timedelta_does_not_cast(td: Any) -> None:
    ...


def test_underlying_data_conversion() -> None:
    ...


def test_preserve_refs(test_data: Any) -> None:
    ...


def test_cast_on_putmask() -> None:
    ...


def test_type_promote_putmask() -> None:
    ...


def test_multilevel_preserve_name() -> None:
    ...


def test_setitem_scalar_into_readonly_backing_data() -> None:
    ...


def test_setitem_slice_into_readonly_backing_data() -> None:
    ...


def test_pop() -> None:
    ...


def test_take() -> None:
    ...


def test_take_categorical() -> None:
    ...


def test_head_tail(test_data: Any) -> None:
    ...
