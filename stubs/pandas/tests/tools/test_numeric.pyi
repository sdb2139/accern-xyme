# Stubs for pandas.tests.tools.test_numeric (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any


def errors(request: Any) -> Any:
    ...


def signed(request: Any) -> Any:
    ...


def transform(request: Any) -> Any:
    ...


def large_val(request: Any) -> Any:
    ...


def multiple_elts(request: Any) -> Any:
    ...


def transform_assert_equal(request: Any) -> Any:
    ...


def test_empty(input_kwargs: Any, result_kwargs: Any) -> None:
    ...


def test_series(last_val: Any) -> None:
    ...


def test_series_numeric(data: Any) -> None:
    ...


def test_error(data: Any, msg: Any) -> None:
    ...


def test_ignore_error(errors: Any, exp_data: Any) -> None:
    ...


def test_bool_handling(errors: Any, exp: Any) -> None:
    ...


def test_list() -> None:
    ...


def test_list_numeric(data: Any, arr_kwargs: Any) -> None:
    ...


def test_numeric(kwargs: Any) -> None:
    ...


def test_numeric_df_columns(columns: Any) -> None:
    ...


def test_numeric_embedded_arr_likes(data: Any, exp_data: Any) -> None:
    ...


def test_all_nan() -> None:
    ...


def test_type_check(errors: Any) -> None:
    ...


def test_scalar(val: Any, signed: Any, transform: Any) -> None:
    ...


def test_really_large_scalar(
        large_val: Any, signed: Any, transform: Any, errors: Any) -> None:
    ...


def test_really_large_in_arr(
        large_val: Any, signed: Any, transform: Any, multiple_elts: Any,
        errors: Any) -> None:
    ...


def test_really_large_in_arr_consistent(
        large_val: Any, signed: Any, multiple_elts: Any, errors: Any) -> None:
    ...


def test_scalar_fail(errors: Any, checker: Any) -> None:
    ...


def test_numeric_dtypes(data: Any, transform_assert_equal: Any) -> None:
    ...


def test_str(data: Any, exp: Any, transform_assert_equal: Any) -> None:
    ...


def test_datetime_like(
        tz_naive_fixture: Any, transform_assert_equal: Any) -> None:
    ...


def test_timedelta(transform_assert_equal: Any) -> None:
    ...


def test_period(transform_assert_equal: Any) -> None:
    ...


def test_non_hashable(errors: Any, expected: Any) -> None:
    ...


def test_downcast_invalid_cast() -> None:
    ...


def test_errors_invalid_value() -> None:
    ...


def test_downcast_basic(data: Any, kwargs: Any, exp_dtype: Any) -> None:
    ...


def test_signed_downcast(data: Any, signed_downcast: Any) -> None:
    ...


def test_ignore_downcast_invalid_data() -> None:
    ...


def test_ignore_downcast_neg_to_unsigned() -> None:
    ...


def test_ignore_downcast_cannot_convert_float(
        data: Any, expected: Any, downcast: Any) -> None:
    ...


def test_downcast_not8bit(downcast: Any, expected_dtype: Any) -> None:
    ...


def test_downcast_limits(dtype: Any, downcast: Any, min_max: Any) -> None:
    ...


def test_coerce_uint64_conflict(data: Any, exp_data: Any) -> None:
    ...


def test_non_coerce_uint64_conflict(errors: Any, exp: Any) -> None:
    ...
