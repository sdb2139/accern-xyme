# Stubs for pandas.tests.frame.test_arithmetic (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any


class TestFrameComparisons:
    def test_comparison_invalid(self) -> None:
        ...

    def test_timestamp_compare(self) -> None:
        ...

    def test_mixed_comparison(self) -> None:
        ...

    def test_df_boolean_comparison_error(self) -> None:
        ...

    def test_df_float_none_comparison(self) -> None:
        ...

    def test_df_string_comparison(self) -> None:
        ...


class TestFrameFlexComparisons:
    def test_bool_flex_frame(self) -> None:
        ...

    def test_flex_comparison_nat(self) -> None:
        ...

    def test_df_flex_cmp_constant_return_types(self, opname: Any) -> None:
        ...

    def test_df_flex_cmp_constant_return_types_empty(self, opname: Any) -> None:
        ...


class TestFrameFlexArithmetic:
    def test_df_add_td64_columnwise(self) -> None:
        ...

    def test_df_add_flex_filled_mixed_dtypes(self) -> None:
        ...

    def test_arith_flex_frame(
            self, all_arithmetic_operators: Any, float_frame: Any,
            mixed_float_frame: Any) -> None:
        ...

    def test_arith_flex_frame_mixed(
            self, op: Any, int_frame: Any, mixed_int_frame: Any,
            mixed_float_frame: Any) -> None:
        ...

    def test_arith_flex_frame_raise(
            self, all_arithmetic_operators: Any, float_frame: Any) -> None:
        ...

    def test_arith_flex_frame_corner(self, float_frame: Any) -> None:
        ...

    def test_arith_flex_series(self, simple_frame: Any) -> None:
        ...

    def test_arith_flex_zero_len_raises(self) -> None:
        ...


class TestFrameArithmetic:
    def test_df_add_2d_array_rowlike_broadcasts(self) -> None:
        ...

    def test_df_add_2d_array_collike_broadcasts(self) -> None:
        ...

    def test_df_arith_2d_array_rowlike_broadcasts(
            self, all_arithmetic_operators: Any) -> None:
        ...

    def test_df_arith_2d_array_collike_broadcasts(
            self, all_arithmetic_operators: Any) -> None:
        ...

    def test_df_bool_mul_int(self) -> None:
        ...

    def test_arith_mixed(self) -> None:
        ...

    def test_arith_getitem_commute(self) -> None:
        ...

    def test_arith_alignment_non_pandas_object(self, values: Any) -> None:
        ...

    def test_arith_non_pandas_object(self) -> None:
        ...
