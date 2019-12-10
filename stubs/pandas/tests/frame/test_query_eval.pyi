# Stubs for pandas.tests.frame.test_query_eval (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any
from pandas.tests.frame.common import TestData

PARSERS: Any
ENGINES: Any


def parser(request: Any) -> Any:
    ...


def engine(request: Any) -> Any:
    ...


def skip_if_no_pandas_parser(parser: Any) -> None:
    ...


class TestCompat:
    df: Any = ...
    expected1: Any = ...
    expected2: Any = ...

    def setup_method(self, method: Any) -> None:
        ...

    def test_query_default(self) -> None:
        ...

    def test_query_None(self) -> None:
        ...

    def test_query_python(self) -> None:
        ...

    def test_query_numexpr(self) -> None:
        ...


class TestDataFrameEval(TestData):
    def test_ops(self) -> None:
        ...

    def test_query_non_str(self):
        ...

    def test_query_empty_string(self) -> None:
        ...

    def test_eval_resolvers_as_list(self) -> None:
        ...


class TestDataFrameQueryWithMultiIndex:
    def test_query_with_named_multiindex(
            self, parser: Any, engine: Any) -> None:
        ...

    def test_query_with_unnamed_multiindex(
            self, parser: Any, engine: Any) -> None:
        ...

    def test_query_with_partially_named_multiindex(
            self, parser: Any, engine: Any) -> None:
        ...

    def test_query_multiindex_get_index_resolvers(self) -> None:
        ...


class TestDataFrameQueryNumExprPandas:
    @classmethod
    def setup_class(cls) -> None:
        ...

    @classmethod
    def teardown_class(cls) -> None:
        ...

    def test_date_query_with_attribute_access(self) -> None:
        ...

    def test_date_query_no_attribute_access(self) -> None:
        ...

    def test_date_query_with_NaT(self) -> None:
        ...

    def test_date_index_query(self) -> None:
        ...

    def test_date_index_query_with_NaT(self) -> None:
        ...

    def test_date_index_query_with_NaT_duplicates(self) -> None:
        ...

    def test_date_query_with_non_date(self) -> None:
        ...

    def test_query_syntax_error(self) -> None:
        ...

    def test_query_scope(self) -> None:
        ...

    def test_query_doesnt_pickup_local(self) -> None:
        ...

    def test_query_builtin(self) -> None:
        ...

    def test_query(self) -> None:
        ...

    def test_query_index_with_name(self) -> None:
        ...

    def test_query_index_without_name(self) -> None:
        ...

    def test_nested_scope(self) -> None:
        ...

    def test_nested_raises_on_local_self_reference(self) -> None:
        ...

    def test_local_syntax(self) -> None:
        ...

    def test_chained_cmp_and_in(self) -> None:
        ...

    def test_local_variable_with_in(self) -> None:
        ...

    def test_at_inside_string(self) -> None:
        ...

    def test_query_undefined_local(self) -> None:
        ...

    def test_index_resolvers_come_after_columns_with_the_same_name(self) -> None:
        ...

    def test_inf(self) -> None:
        ...


class TestDataFrameQueryNumExprPython(TestDataFrameQueryNumExprPandas):
    @classmethod
    def setup_class(cls) -> None:
        ...

    def test_date_query_no_attribute_access(self) -> None:
        ...

    def test_date_query_with_NaT(self) -> None:
        ...

    def test_date_index_query(self) -> None:
        ...

    def test_date_index_query_with_NaT(self) -> None:
        ...

    def test_date_index_query_with_NaT_duplicates(self) -> None:
        ...

    def test_nested_scope(self) -> None:
        ...


class TestDataFrameQueryPythonPandas(TestDataFrameQueryNumExprPandas):
    @classmethod
    def setup_class(cls) -> None:
        ...

    def test_query_builtin(self) -> None:
        ...


class TestDataFrameQueryPythonPython(TestDataFrameQueryNumExprPython):
    @classmethod
    def setup_class(cls) -> None:
        ...

    def test_query_builtin(self) -> None:
        ...


class TestDataFrameQueryStrings:
    def test_str_query_method(self, parser: Any, engine: Any) -> None:
        ...

    def test_str_list_query_method(self, parser: Any, engine: Any) -> None:
        ...

    def test_query_with_string_columns(self, parser: Any, engine: Any) -> None:
        ...

    def test_object_array_eq_ne(self, parser: Any, engine: Any) -> None:
        ...

    def test_query_with_nested_strings(self, parser: Any, engine: Any) -> None:
        ...

    def test_query_with_nested_special_character(
            self, parser: Any, engine: Any) -> None:
        ...

    def test_query_lex_compare_strings(self, parser: Any, engine: Any) -> None:
        ...

    def test_query_single_element_booleans(
            self, parser: Any, engine: Any) -> None:
        ...

    def test_query_string_scalar_variable(
            self, parser: Any, engine: Any) -> None:
        ...


class TestDataFrameEvalWithFrame:
    frame: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def teardown_method(self, method: Any) -> None:
        ...

    def test_simple_expr(self, parser: Any, engine: Any) -> None:
        ...

    def test_bool_arith_expr(self, parser: Any, engine: Any) -> None:
        ...

    def test_invalid_type_for_operator_raises(
            self, parser: Any, engine: Any, op: Any) -> None:
        ...


class TestDataFrameQueryBacktickQuoting:
    def df(self) -> None:
        ...

    def test_single_backtick_variable_query(self, df: Any) -> None:
        ...

    def test_two_backtick_variables_query(self, df: Any) -> None:
        ...

    def test_single_backtick_variable_expr(self, df: Any) -> None:
        ...

    def test_two_backtick_variables_expr(self, df: Any) -> None:
        ...

    def test_already_underscore_variable(self, df: Any) -> None:
        ...

    def test_same_name_but_underscores(self, df: Any) -> None:
        ...

    def test_mixed_underscores_and_spaces(self, df: Any) -> None:
        ...

    def backtick_quote_name_with_no_spaces(self, df: Any) -> None:
        ...
