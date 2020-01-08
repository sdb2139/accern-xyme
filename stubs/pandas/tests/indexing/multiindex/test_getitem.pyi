# Stubs for pandas.tests.indexing.multiindex.test_getitem (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

def test_series_getitem_multiindex(access_method: Any, level1_value: Any, expected: Any) -> None:
    ...


def test_series_getitem_duplicates_multiindex(level0_value: Any) -> None:
    ...


def test_series_getitem(multiindex_year_month_day_dataframe_random_data: Any, indexer: Any) -> None:
    ...


def test_series_getitem_returns_scalar(multiindex_year_month_day_dataframe_random_data: Any, indexer: Any) -> None:
    ...


def test_series_getitem_indexing_errors(multiindex_year_month_day_dataframe_random_data: Any, indexer: Any, expected_error: Any, expected_error_msg: Any) -> None:
    ...


def test_series_getitem_corner_generator(multiindex_year_month_day_dataframe_random_data: Any) -> None:
    ...


def test_getitem_simple(multiindex_dataframe_random_data: Any) -> None:
    ...


def test_frame_getitem_simple_key_error(multiindex_dataframe_random_data: Any, indexer: Any, expected_error_msg: Any) -> None:
    ...


def test_frame_getitem_multicolumn_empty_level() -> None:
    ...


def test_frame_getitem_toplevel(multiindex_dataframe_random_data: Any, indexer: Any, expected_slice: Any) -> None:
    ...


def test_frame_mixed_depth_get() -> None:
    ...


def dataframe_with_duplicate_index():
    ...


def test_frame_mi_access(dataframe_with_duplicate_index: Any, indexer: Any) -> None:
    ...


def test_frame_mi_access_returns_series(dataframe_with_duplicate_index: Any) -> None:
    ...


def test_frame_mi_access_returns_frame(dataframe_with_duplicate_index: Any) -> None:
    ...