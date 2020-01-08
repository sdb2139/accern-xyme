# Stubs for pandas.tests.io.parser.test_na_values (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

def test_string_nas(all_parsers: Any) -> None:
    ...


def test_detect_string_na(all_parsers: Any) -> None:
    ...


def test_non_string_na_values(all_parsers: Any, data: Any, na_values: Any) -> None:
    ...


def test_default_na_values(all_parsers: Any) -> None:
    ...


def test_custom_na_values(all_parsers: Any, na_values: Any) -> None:
    ...


def test_bool_na_values(all_parsers: Any) -> None:
    ...


def test_na_value_dict(all_parsers: Any) -> None:
    ...


def test_na_value_dict_multi_index(all_parsers: Any, index_col: Any, expected: Any) -> None:
    ...


def test_na_values_keep_default(all_parsers: Any, kwargs: Any, expected: Any) -> None:
    ...


def test_no_na_values_no_keep_default(all_parsers: Any) -> None:
    ...


def test_no_keep_default_na_dict_na_values(all_parsers: Any) -> None:
    ...


def test_no_keep_default_na_dict_na_scalar_values(all_parsers: Any) -> None:
    ...


def test_no_keep_default_na_dict_na_values_diff_reprs(all_parsers: Any, col_zero_na_values: Any) -> None:
    ...


def test_na_values_na_filter_override(all_parsers: Any, na_filter: Any, row_data: Any) -> None:
    ...


def test_na_trailing_columns(all_parsers: Any) -> None:
    ...


def test_na_values_scalar(all_parsers: Any, na_values: Any, row_data: Any) -> None:
    ...


def test_na_values_dict_aliasing(all_parsers: Any) -> None:
    ...


def test_na_values_dict_col_index(all_parsers: Any) -> None:
    ...


def test_na_values_uint64(all_parsers: Any, data: Any, kwargs: Any, expected: Any) -> None:
    ...


def test_empty_na_values_no_default_with_index(all_parsers: Any) -> None:
    ...


def test_no_na_filter_on_index(all_parsers: Any, na_filter: Any, index_data: Any) -> None:
    ...


def test_inf_na_values_with_int_index(all_parsers: Any) -> None:
    ...


def test_na_values_with_dtype_str_and_na_filter(all_parsers: Any, na_filter: Any) -> None:
    ...


def test_cast_NA_to_bool_raises_error(all_parsers: Any, data: Any, na_values: Any) -> None:
    ...