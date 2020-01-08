# Stubs for pandas.tests.frame.test_missing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,redefined-builtin

from typing import Any


class TestDataFrameMissingData:
    def test_dropEmptyRows(self, float_frame: Any) -> None:
        ...

    def test_dropIncompleteRows(self, float_frame: Any) -> None:
        ...

    def test_dropna(self) -> None:
        ...

    def test_drop_and_dropna_caching(self) -> None:
        ...

    def test_dropna_corner(self, float_frame: Any) -> None:
        ...

    def test_dropna_multiple_axes(self) -> None:
        ...

    def test_dropna_tz_aware_datetime(self) -> None:
        ...

    def test_dropna_categorical_interval_index(self) -> None:
        ...

    def test_fillna_datetime(self, datetime_frame: Any) -> None:
        ...

    def test_fillna_mixed_type(self, float_string_frame: Any) -> None:
        ...

    def test_fillna_mixed_float(self, mixed_float_frame: Any) -> None:
        ...

    def test_fillna_empty(self) -> None:
        ...

    def test_fillna_different_dtype(self) -> None:
        ...

    def test_fillna_limit_and_value(self) -> None:
        ...

    def test_fillna_datelike(self) -> None:
        ...

    def test_fillna_tzaware(self) -> None:
        ...

    def test_fillna_tzaware_different_column(self) -> None:
        ...

    def test_na_actions_categorical(self) -> None:
        ...

    def test_fillna_categorical_nan(self) -> None:
        ...

    def test_fillna_downcast(self) -> None:
        ...

    def test_fillna_dtype_conversion(self) -> None:
        ...

    def test_fillna_datetime_columns(self) -> None:
        ...

    def test_ffill(self, datetime_frame: Any) -> None:
        ...

    def test_bfill(self, datetime_frame: Any) -> None:
        ...

    def test_frame_pad_backfill_limit(self) -> None:
        ...

    def test_frame_fillna_limit(self) -> None:
        ...

    def test_fillna_skip_certain_blocks(self) -> None:
        ...

    def test_fillna_positive_limit(self, type: Any) -> None:
        ...

    def test_fillna_integer_limit(self, type: Any) -> None:
        ...

    def test_fillna_inplace(self) -> None:
        ...

    def test_fillna_dict_series(self) -> None:
        ...

    def test_fillna_dataframe(self) -> None:
        ...

    def test_fillna_columns(self) -> None:
        ...

    def test_fillna_invalid_method(self, float_frame: Any) -> None:
        ...

    def test_fillna_invalid_value(self, float_frame: Any) -> None:
        ...

    def test_fillna_col_reordering(self) -> None:
        ...

    def test_fill_corner(
            self, float_frame: Any, float_string_frame: Any) -> None:
        ...

    def test_fill_value_when_combine_const(self) -> None:
        ...


class TestDataFrameInterpolate:
    def test_interp_basic(self) -> None:
        ...

    def test_interp_bad_method(self) -> None:
        ...

    def test_interp_combo(self) -> None:
        ...

    def test_interp_nan_idx(self) -> None:
        ...

    def test_interp_various(self) -> None:
        ...

    def test_interp_alt_scipy(self) -> None:
        ...

    def test_interp_rowwise(self) -> None:
        ...

    def test_rowwise_alt(self) -> None:
        ...

    def test_interp_leading_nans(self, check_scipy: Any) -> None:
        ...

    def test_interp_raise_on_only_mixed(self) -> None:
        ...

    def test_interp_raise_on_all_object_dtype(self) -> None:
        ...

    def test_interp_inplace(self) -> None:
        ...

    def test_interp_inplace_row(self) -> None:
        ...

    def test_interp_ignore_all_good(self) -> None:
        ...