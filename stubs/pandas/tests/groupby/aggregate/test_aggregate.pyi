# Stubs for pandas.tests.groupby.aggregate.test_aggregate (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any

def test_agg_regression1(tsframe: Any) -> None:
    ...


def test_agg_must_agg(df: Any) -> None:
    ...


def test_agg_ser_multi_key(df: Any) -> None:
    ...


def test_groupby_aggregation_mixed_dtype() -> None:
    ...


def test_agg_apply_corner(ts: Any, tsframe: Any) -> None:
    ...


def test_agg_grouping_is_list_tuple(ts: Any) -> None:
    ...


def test_agg_python_multiindex(mframe: Any) -> None:
    ...


def test_aggregate_str_func(tsframe: Any, groupbyfunc: Any) -> None:
    ...


def test_aggregate_item_by_item(df: Any) -> None:
    ...


def test_wrap_agg_out(three_group: Any) -> None:
    ...


def test_agg_multiple_functions_maintain_order(df: Any) -> None:
    ...


def test_multiple_functions_tuples_and_non_tuples(df: Any) -> None:
    ...


def test_more_flexible_frame_multi_function(df: Any) -> None:
    ...


def test_multi_function_flexible_mix(df: Any) -> None:
    ...


def test_groupby_agg_coercing_bools() -> None:
    ...


def test_order_aggregate_multiple_funcs() -> None:
    ...


def test_uint64_type_handling(dtype: Any, how: Any) -> None:
    ...



class TestNamedAggregationSeries:
    def test_series_named_agg(self) -> None:
        ...

    def test_no_args_raises(self) -> None:
        ...

    def test_series_named_agg_duplicates_raises(self) -> None:
        ...

    def test_mangled(self) -> None:
        ...


class TestNamedAggregationDataFrame:
    def test_agg_relabel(self) -> None:
        ...

    def test_agg_relabel_non_identifier(self) -> None:
        ...

    def test_duplicate_raises(self) -> None:
        ...

    def test_agg_relabel_with_level(self) -> None:
        ...

    def test_agg_relabel_other_raises(self) -> None:
        ...

    def test_missing_raises(self) -> None:
        ...

    def test_agg_namedtuple(self) -> None:
        ...

    def test_mangled(self) -> None:
        ...



class TestLambdaMangling:
    def test_maybe_mangle_lambdas_passthrough(self) -> None:
        ...

    def test_maybe_mangle_lambdas_listlike(self) -> None:
        ...

    def test_maybe_mangle_lambdas(self) -> None:
        ...

    def test_maybe_mangle_lambdas_args(self) -> None:
        ...

    def test_maybe_mangle_lambdas_named(self) -> None:
        ...

    def test_basic(self) -> None:
        ...

    def test_mangle_series_groupby(self) -> None:
        ...

    def test_with_kwargs(self) -> None:
        ...
