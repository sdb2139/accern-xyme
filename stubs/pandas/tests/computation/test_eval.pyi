# Stubs for pandas.tests.computation.test_eval (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,import-error

from typing import Any


def engine(request: Any) -> Any:
    ...


def parser(request: Any) -> Any:
    ...


def ne_lt_2_6_9() -> Any:
    ...


def unary_fns_for_ne() -> Any:
    ...


def engine_has_neg_frac(engine: Any) -> Any:
    ...


class TestEvalNumexprPandas:
    @classmethod
    def setup_class(cls) -> None:
        ...

    @classmethod
    def teardown_class(cls) -> None:
        ...

    pandas_lhses: Any = ...
    pandas_rhses: Any = ...
    scalar_lhses: Any = ...
    scalar_rhses: Any = ...
    lhses: Any = ...
    rhses: Any = ...
    def setup_data(self) -> None:
        ...

    cmp_ops: Any = ...
    cmp2_ops: Any = ...
    bin_ops: Any = ...
    special_case_ops: Any = ...
    arith_ops: Any = ...
    unary_ops: Any = ...
    def setup_ops(self) -> None:
        ...

    current_engines: Any = ...
    def setup_method(self, method: Any) -> Any:
        ...

    def teardown_method(self, method: Any) -> None:
        ...

    def test_complex_cmp_ops(self, cmp1: Any, cmp2: Any) -> None:
        ...

    def test_simple_cmp_ops(self) -> None:
        ...

    def test_binary_arith_ops(self) -> None:
        ...

    def test_modulus(self) -> None:
        ...

    def test_floor_division(self) -> None:
        ...

    def test_pow(self) -> None:
        ...

    def test_single_invert_op(self) -> None:
        ...

    def test_compound_invert_op(self) -> None:
        ...

    def test_chained_cmp_op(self) -> None:
        ...

    def check_equal(self, result: Any, expected: Any) -> None:
        ...

    def check_chained_cmp_op(
            self, lhs: Any, cmp1: Any, mid: Any, cmp2: Any, rhs: Any) -> None:
        ...

    def check_simple_cmp_op(self, lhs: Any, cmp1: Any, rhs: Any) -> None:
        ...

    def check_binary_arith_op(self, lhs: Any, arith1: Any, rhs: Any) -> None:
        ...

    def check_alignment(
            self, result: Any, nlhs: Any, ghs: Any, op: Any) -> None:
        ...

    def check_modulus(self, lhs: Any, arith1: Any, rhs: Any) -> None:
        ...

    def check_floor_division(self, lhs: Any, arith1: Any, rhs: Any) -> None:
        ...

    def get_expected_pow_result(self, lhs: Any, rhs: Any) -> Any:
        ...

    def check_pow(self, lhs: Any, arith1: Any, rhs: Any) -> None:
        ...

    def check_single_invert_op(self, lhs: Any, cmp1: Any, rhs: Any) -> None:
        ...

    def check_compound_invert_op(self, lhs: Any, cmp1: Any, rhs: Any) -> None:
        ...

    def ex(self, op: Any, var_name: str = ...) -> Any:
        ...

    def test_frame_invert(self) -> None:
        ...

    def test_series_invert(self) -> None:
        ...

    def test_frame_negate(self) -> None:
        ...

    def test_series_negate(self) -> None:
        ...

    def test_frame_pos(self) -> None:
        ...

    def test_series_pos(self) -> None:
        ...

    def test_scalar_unary(self) -> None:
        ...

    def test_unary_in_array(self) -> None:
        ...

    def test_float_comparison_bin_op(self, dtype: Any) -> None:
        ...

    def test_disallow_scalar_bool_ops(self) -> None:
        ...

    def test_identical(self) -> None:
        ...

    def test_line_continuation(self) -> None:
        ...

    def test_float_truncation(self) -> None:
        ...

    def test_disallow_python_keywords(self) -> None:
        ...


class TestEvalNumexprPython(TestEvalNumexprPandas):
    @classmethod
    def setup_class(cls) -> None:
        ...

    cmp_ops: Any = ...
    cmp2_ops: Any = ...
    bin_ops: Any = ...
    special_case_ops: Any = ...
    arith_ops: Any = ...
    unary_ops: Any = ...

    def setup_ops(self):
        ...

    def check_chained_cmp_op(
            self, lhs: Any, cmp1: Any, mid: Any, cmp2: Any, rhs: Any) -> None:
        ...


class TestEvalPythonPython(TestEvalNumexprPython):
    @classmethod
    def setup_class(cls) -> None:
        ...

    def check_modulus(self, lhs: Any, arith1: Any, rhs: Any) -> None:
        ...

    def check_alignment(
            self, result: Any, nlhs: Any, ghs: Any, op: Any) -> None:
        ...


class TestEvalPythonPandas(TestEvalPythonPython):
    @classmethod
    def setup_class(cls) -> None:
        ...

    def check_chained_cmp_op(
            self, lhs: Any, cmp1: Any, mid: Any, cmp2: Any, rhs: Any) -> None:
        ...


f: Any

class TestTypeCasting:
    def test_binop_typecasting(
            self, engine: Any, parser: Any, op: Any, dt: Any) -> None:
        ...


def should_warn(*args: Any) -> Any:
    ...


class TestAlignment:
    index_types: Any = ...
    lhs_index_types: Any = ...

    def test_align_nested_unary_op(self, engine: Any, parser: Any) -> None:
        ...

    def test_basic_frame_alignment(self, engine: Any, parser: Any) -> None:
        ...

    def test_frame_comparison(self, engine: Any, parser: Any) -> None:
        ...

    def test_medium_complex_frame_alignment(
            self, engine: Any, parser: Any) -> None:
        ...

    def test_basic_frame_series_alignment(
            self, engine: Any, parser: Any) -> None:
        ...

    def test_basic_series_frame_alignment(
            self, engine: Any, parser: Any) -> None:
        ...

    def test_series_frame_commutativity(
            self, engine: Any, parser: Any) -> None:
        ...

    def test_complex_series_frame_alignment(
            self, engine: Any, parser: Any) -> None:
        ...

    def test_performance_warning_for_poor_alignment(
            self, engine: Any, parser: Any) -> None:
        ...


class TestOperationsNumExprPandas:
    @classmethod
    def setup_class(cls) -> None:
        ...

    @classmethod
    def teardown_class(cls) -> None:
        ...

    def eval(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def test_simple_arith_ops(self):
        ...

    def test_simple_bool_ops(self) -> None:
        ...

    def test_bool_ops_with_constants(self) -> None:
        ...

    def test_4d_ndarray_fails(self) -> None:
        ...

    def test_constant(self) -> None:
        ...

    def test_single_variable(self) -> None:
        ...

    def test_truediv(self) -> None:
        ...

    def test_failing_subscript_with_name_error(self) -> None:
        ...

    def test_lhs_expression_subscript(self) -> None:
        ...

    def test_attr_expression(self) -> None:
        ...

    def test_assignment_fails(self) -> None:
        ...

    def test_assignment_column(self):
        ...

    def test_column_in(self) -> None:
        ...

    def assignment_not_inplace(self) -> None:
        ...

    def test_multi_line_expression(self) -> None:
        ...

    def test_multi_line_expression_not_inplace(self) -> None:
        ...

    def test_multi_line_expression_local_variable(self) -> None:
        ...

    def test_multi_line_expression_callable_local_variable(self) -> None:
        ...

    def test_multi_line_expression_callable_local_variable_with_kwargs(
            self) -> None:
        ...

    def test_assignment_in_query(self) -> None:
        ...

    def test_query_inplace(self) -> None:
        ...

    def test_cannot_item_assign(self, invalid_target: Any) -> None:
        ...

    def test_cannot_copy_item(self, invalid_target: Any) -> None:
        ...

    def test_inplace_no_assignment(self, target: Any) -> None:
        ...

    def test_basic_period_index_boolean_expression(self) -> None:
        ...

    def test_basic_period_index_subscript_expression(self) -> None:
        ...

    def test_nested_period_index_subscript_expression(self) -> None:
        ...

    def test_date_boolean(self) -> None:
        ...

    def test_simple_in_ops(self) -> None:
        ...


class TestOperationsNumExprPython(TestOperationsNumExprPandas):
    @classmethod
    def setup_class(cls):
        ...

    def test_check_many_exprs(self) -> None:
        ...

    def test_fails_and(self) -> None:
        ...

    def test_fails_or(self) -> None:
        ...

    def test_fails_not(self) -> None:
        ...

    def test_fails_ampersand(self) -> None:
        ...

    def test_fails_pipe(self) -> None:
        ...

    def test_bool_ops_with_constants(self) -> None:
        ...

    def test_simple_bool_ops(self) -> None:
        ...


class TestOperationsPythonPython(TestOperationsNumExprPython):
    @classmethod
    def setup_class(cls):
        ...


class TestOperationsPythonPandas(TestOperationsNumExprPandas):
    @classmethod
    def setup_class(cls) -> None:
        ...


class TestMathPythonPython:
    @classmethod
    def setup_class(cls) -> None:
        ...

    @classmethod
    def teardown_class(cls) -> None:
        ...

    def eval(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def test_unary_functions(self, unary_fns_for_ne: Any) -> None:
        ...

    def test_floor_and_ceil_functions_raise_error(
            self, ne_lt_2_6_9: Any, unary_fns_for_ne: Any) -> None:
        ...

    def test_binary_functions(self) -> None:
        ...

    def test_df_use_case(self) -> None:
        ...

    def test_df_arithmetic_subexpression(self) -> None:
        ...

    def check_result_type(self, dtype: Any, expect_dtype: Any) -> None:
        ...

    def test_result_types(self) -> None:
        ...

    def test_result_types2(self) -> None:
        ...

    def test_undefined_func(self) -> None:
        ...

    def test_keyword_arg(self) -> None:
        ...


class TestMathPythonPandas(TestMathPythonPython):
    @classmethod
    def setup_class(cls) -> None:
        ...


class TestMathNumExprPandas(TestMathPythonPython):
    @classmethod
    def setup_class(cls) -> None:
        ...


class TestMathNumExprPython(TestMathPythonPython):
    @classmethod
    def setup_class(cls) -> None:
        ...


class TestScope:
    def test_global_scope(self, engine: Any, parser: Any) -> None:
        ...

    def test_no_new_locals(self, engine: Any, parser: Any) -> None:
        ...

    def test_no_new_globals(self, engine: Any, parser: Any) -> None:
        ...


def test_invalid_engine() -> None:
    ...


def test_invalid_parser() -> None:
    ...


def test_disallowed_nodes(engine: Any, parser: Any) -> None:
    ...


def test_syntax_error_exprs(engine: Any, parser: Any) -> None:
    ...


def test_name_error_exprs(engine: Any, parser: Any) -> None:
    ...


def test_invalid_local_variable_reference(engine: Any, parser: Any) -> None:
    ...


def test_numexpr_builtin_raises(engine: Any, parser: Any) -> None:
    ...


def test_bad_resolver_raises(engine: Any, parser: Any) -> None:
    ...


def test_empty_string_raises(engine: Any, parser: Any) -> None:
    ...


def test_more_than_one_expression_raises(engine: Any, parser: Any) -> None:
    ...


def test_bool_ops_fails_on_scalars(
        lhs: Any, cmp: Any, rhs: Any, engine: Any, parser: Any) -> None:
    ...


def test_inf(engine: Any, parser: Any) -> None:
    ...


def test_negate_lt_eq_le(engine: Any, parser: Any) -> None:
    ...


class TestValidate:
    def test_validate_bool_args(self) -> None:
        ...
