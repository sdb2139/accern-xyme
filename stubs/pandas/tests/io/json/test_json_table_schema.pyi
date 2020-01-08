# Stubs for pandas.tests.io.json.test_json_table_schema (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

class TestBuildSchema:
    df: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def test_build_table_schema(self) -> None:
        ...

    def test_series(self) -> None:
        ...

    def test_series_unnamed(self) -> None:
        ...

    def test_multiindex(self) -> None:
        ...


class TestTableSchemaType:
    def test_as_json_table_type_int_data(self, int_type: Any) -> None:
        ...

    def test_as_json_table_type_float_data(self, float_type: Any) -> None:
        ...

    def test_as_json_table_type_bool_data(self, bool_type: Any) -> None:
        ...

    def test_as_json_table_type_date_data(self, date_data: Any) -> None:
        ...

    def test_as_json_table_type_string_data(self, str_data: Any) -> None:
        ...

    def test_as_json_table_type_categorical_data(self, cat_data: Any) -> None:
        ...

    def test_as_json_table_type_int_dtypes(self, int_dtype: Any) -> None:
        ...

    def test_as_json_table_type_float_dtypes(self, float_dtype: Any) -> None:
        ...

    def test_as_json_table_type_bool_dtypes(self, bool_dtype: Any) -> None:
        ...

    def test_as_json_table_type_date_dtypes(self, date_dtype: Any) -> None:
        ...

    def test_as_json_table_type_timedelta_dtypes(self, td_dtype: Any) -> None:
        ...

    def test_as_json_table_type_string_dtypes(self, str_dtype: Any) -> None:
        ...

    def test_as_json_table_type_categorical_dtypes(self) -> None:
        ...


class TestTableOrient:
    df: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def test_build_series(self) -> None:
        ...

    def test_to_json(self) -> None:
        ...

    def test_to_json_float_index(self) -> None:
        ...

    def test_to_json_period_index(self) -> None:
        ...

    def test_to_json_categorical_index(self) -> None:
        ...

    def test_date_format_raises(self) -> None:
        ...

    def test_convert_pandas_type_to_json_field_int(self, kind: Any) -> None:
        ...

    def test_convert_pandas_type_to_json_field_float(self, kind: Any) -> None:
        ...

    def test_convert_pandas_type_to_json_field_datetime(self, dt_args: Any, extra_exp: Any, wrapper: Any) -> None:
        ...

    def test_convert_pandas_type_to_json_period_range(self) -> None:
        ...

    def test_convert_pandas_type_to_json_field_categorical(self, kind: Any, ordered: Any) -> None:
        ...

    def test_convert_json_field_to_pandas_type(self, inp: Any, exp: Any) -> None:
        ...

    def test_convert_json_field_to_pandas_type_raises(self, inp: Any) -> None:
        ...

    def test_categorical(self) -> None:
        ...

    def test_set_names_unset(self, idx: Any, nm: Any, prop: Any) -> None:
        ...

    def test_warns_non_roundtrippable_names(self, idx: Any) -> None:
        ...

    def test_timestamp_in_columns(self) -> None:
        ...

    def test_overlapping_names(self, case: Any) -> None:
        ...

    def test_mi_falsey_name(self) -> None:
        ...


class TestTableOrientReader:
    def test_read_json_table_orient(self, index_nm: Any, vals: Any, recwarn: Any) -> None:
        ...

    def test_read_json_table_orient_raises(self, index_nm: Any, vals: Any, recwarn: Any) -> None:
        ...

    def test_comprehensive(self) -> None:
        ...

    def test_multiindex(self, index_names: Any) -> None:
        ...

    def test_empty_frame_roundtrip(self) -> None:
        ...