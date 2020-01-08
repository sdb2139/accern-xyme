# Stubs for pandas.tests.test_expressions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any, Optional

class TestExpressions:
    frame: Any = ...
    frame2: Any = ...
    mixed: Any = ...
    mixed2: Any = ...
    integer: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def teardown_method(self, method: Any) -> None:
        ...

    def run_arithmetic(
            self, df: Any, other: Any, assert_func: Any,
            check_dtype: bool = ..., test_flex: bool = ...) -> None:
        ...

    def test_integer_arithmetic(self) -> None:
        ...

    def run_binary(
            self, df: Any, other: Any, assert_func: Any, test_flex: bool = ...,
            numexpr_ops: Any = ...) -> None:
        ...

    def run_frame(
            self, df: Any, other: Any, binary_comp: Optional[Any] = ...,
            run_binary: bool = ..., **kwargs: Any) -> None:
        ...

    def run_series(
            self, ser: Any, other: Any, binary_comp: Optional[Any] = ...,
            **kwargs: Any) -> None:
        ...

    def test_integer_arithmetic_frame(self) -> None:
        ...

    def test_integer_arithmetic_series(self) -> None:
        ...

    def test_float_arithemtic_frame(self) -> None:
        ...

    def test_float_arithmetic_series(self) -> None:
        ...

    def test_mixed_arithmetic_frame(self) -> None:
        ...

    def test_mixed_arithmetic_series(self) -> None:
        ...

    def test_float_arithemtic(self) -> None:
        ...

    def test_mixed_arithmetic(self) -> None:
        ...

    def test_integer_with_zeros(self) -> None:
        ...

    def test_invalid(self) -> None:
        ...

    def test_binary_ops(self) -> None:
        ...

    def test_boolean_ops(self) -> None:
        ...

    def test_where(self) -> None:
        ...

    def test_bool_ops_raise_on_arithmetic(self) -> None:
        ...

    def test_bool_ops_warn_on_arithmetic(self) -> None:
        ...

    def test_bool_ops_column_name_dtype(
            self, test_input: Any, expected: Any) -> None:
        ...