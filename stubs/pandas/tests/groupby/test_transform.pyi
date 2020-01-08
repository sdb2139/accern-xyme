# Stubs for pandas.tests.groupby.test_transform (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,redefined-builtin

from typing import Any


def assert_fp_equal(a: Any, b: Any) -> None:
    ...


def test_transform() -> None:
    ...


def test_transform_fast() -> None:
    ...


def test_transform_broadcast(tsframe: Any, ts: Any) -> None:
    ...


def test_transform_axis(tsframe: Any) -> None:
    ...


def test_transform_dtype() -> None:
    ...


def test_transform_bug() -> None:
    ...


def test_transform_numeric_to_boolean() -> None:
    ...


def test_transform_datetime_to_timedelta() -> None:
    ...


def test_transform_datetime_to_numeric() -> None:
    ...


def test_transform_casting() -> None:
    ...


def test_transform_multiple(ts: Any) -> None:
    ...


def test_dispatch_transform(tsframe: Any) -> None:
    ...


def test_transform_select_columns(df: Any) -> None:
    ...


def test_transform_exclude_nuisance(df: Any) -> None:
    ...


def test_transform_function_aliases(df: Any) -> None:
    ...


def test_series_fast_transform_date() -> None:
    ...


def test_transform_length() -> None:
    ...


def test_transform_coercion() -> None:
    ...


def test_groupby_transform_with_int() -> None:
    ...


def test_groupby_transform_with_nan_group() -> None:
    ...


def test_transform_mixed_type() -> None:
    ...


def test_cython_group_transform_cumsum(any_real_dtype: Any) -> None:
    ...


def test_cython_group_transform_cumprod() -> None:
    ...


def test_cython_group_transform_algos() -> None:
    ...


def test_cython_transform_series(op: Any, args: Any, targop: Any) -> None:
    ...


def test_groupby_cum_skipna(
        op: Any, skipna: Any, input: Any, exp: Any) -> None:
    ...


def test_cython_transform_frame(op: Any, args: Any, targop: Any) -> None:
    ...


def test_transform_with_non_scalar_group() -> None:
    ...


def test_transform_numeric_ret(
        cols: Any, exp: Any, comp_func: Any, agg_func: Any) -> None:
    ...


def test_group_fill_methods(
        mix_groupings: Any, as_series: Any, val1: Any, val2: Any,
        fill_method: Any, limit: Any, exp_vals: Any) -> None:
    ...


def test_pad_stable_sorting(fill_method: Any) -> None:
    ...


def test_pct_change(
        test_series: Any, freq: Any, periods: Any, fill_method: Any,
        limit: Any) -> None:
    ...


def test_any_all_np_func(func: Any) -> None:
    ...


def test_groupby_transform_rename() -> None:
    ...


def test_groupby_transform_timezone_column(func: Any) -> None:
    ...


def test_groupby_transform_with_datetimes(func: Any, values: Any) -> None:
    ...


def test_transform_absent_categories(func: Any) -> None:
    ...


def test_ffill_not_in_axis(func: Any, key: Any, val: Any) -> None:
    ...