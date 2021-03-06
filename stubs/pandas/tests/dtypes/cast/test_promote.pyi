# Stubs for pandas.tests.dtypes.cast.test_promote (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name

from typing import Any


def any_numpy_dtype_reduced(request: Any) -> Any:
    ...


def box(request: Any) -> Any:
    ...


def test_maybe_promote_int_with_int() -> None:
    ...


def test_maybe_promote_int_with_float(
        any_int_dtype: Any, float_dtype: Any, box: Any) -> None:
    ...


def test_maybe_promote_float_with_int(
        float_dtype: Any, any_int_dtype: Any, box: Any) -> None:
    ...


def test_maybe_promote_float_with_float() -> None:
    ...


def test_maybe_promote_bool_with_any(
        any_numpy_dtype_reduced: Any, box: Any) -> None:
    ...


def test_maybe_promote_any_with_bool(
        any_numpy_dtype_reduced: Any, box: Any) -> None:
    ...


def test_maybe_promote_bytes_with_any() -> None:
    ...


def test_maybe_promote_any_with_bytes() -> None:
    ...


def test_maybe_promote_datetime64_with_any() -> None:
    ...


def test_maybe_promote_any_with_datetime64(
        any_numpy_dtype_reduced: Any, datetime64_dtype: Any,
        fill_value: Any, box: Any) -> None:
    ...


def test_maybe_promote_datetimetz_with_any_numpy_dtype(
        tz_aware_fixture: Any, any_numpy_dtype_reduced: Any, box: Any) -> None:
    ...


def test_maybe_promote_datetimetz_with_datetimetz(
        tz_aware_fixture: Any, tz_aware_fixture2: Any, box: Any) -> None:
    ...


def test_maybe_promote_datetimetz_with_na(
        tz_aware_fixture: Any, fill_value: Any, box: Any) -> None:
    ...


def test_maybe_promote_any_numpy_dtype_with_datetimetz(
        any_numpy_dtype_reduced: Any, tz_aware_fixture: Any, fill_value: Any,
        box: Any) -> None:
    ...


def test_maybe_promote_timedelta64_with_any() -> None:
    ...


def test_maybe_promote_any_with_timedelta64(
        any_numpy_dtype_reduced: Any, timedelta64_dtype: Any, fill_value: Any,
        box: Any) -> None:
    ...


def test_maybe_promote_string_with_any(
        string_dtype: Any, any_numpy_dtype_reduced: Any, box: Any) -> None:
    ...


def test_maybe_promote_any_with_string(
        any_numpy_dtype_reduced: Any, string_dtype: Any, box: Any) -> None:
    ...


def test_maybe_promote_object_with_any(
        object_dtype: Any, any_numpy_dtype_reduced: Any, box: Any) -> None:
    ...


def test_maybe_promote_any_with_object(
        any_numpy_dtype_reduced: Any, object_dtype: Any, box: Any) -> None:
    ...


def test_maybe_promote_any_numpy_dtype_with_na(
        any_numpy_dtype_reduced: Any, fill_value: Any, box: Any) -> None:
    ...


def test_maybe_promote_dimensions(
        any_numpy_dtype_reduced: Any, dim: Any) -> None:
    ...
