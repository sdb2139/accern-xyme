# Stubs for pandas.tests.frame.test_analytics (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level


from typing import Any, Optional

def assert_stat_op_calc(
        opname: Any, alternative: Any, frame: Any, has_skipna: bool = ...,
        check_dtype: bool = ..., check_dates: bool = ...,
        check_less_precise: bool = ...,
        skipna_alternative: Optional[Any] = ...) -> None:
    ...


def assert_stat_op_api(
        opname: Any, float_frame: Any, float_string_frame: Any,
        has_numeric_only: bool = ...) -> None:
    ...


def assert_bool_op_calc(
        opname: Any, alternative: Any, frame: Any,
        has_skipna: bool = ...) -> None:
    ...


def assert_bool_op_api(
        opname: Any, bool_frame_with_na: Any, float_string_frame: Any,
        has_bool_only: bool = ...) -> None:
    ...


class TestDataFrameAnalytics:
    def test_corr_pearson(self, float_frame: Any) -> None:
        ...

    def test_corr_kendall(self, float_frame: Any) -> None:
        ...

    def test_corr_spearman(self, float_frame: Any) -> None:
        ...

    def test_corr_non_numeric(
            self, float_frame: Any, float_string_frame: Any) -> None:
        ...

    def test_corr_nooverlap(self, meth: Any) -> None:
        ...

    def test_corr_constant(self, meth: Any) -> None:
        ...

    def test_corr_int(self) -> None:
        ...

    def test_corr_int_and_boolean(self) -> None:
        ...

    def test_corr_cov_independent_index_column(self) -> None:
        ...

    def test_corr_invalid_method(self) -> None:
        ...

    def test_cov(self, float_frame: Any, float_string_frame: Any) -> None:
        ...

    def test_corrwith(self, datetime_frame: Any) -> None:
        ...

    def test_corrwith_with_objects(self) -> None:
        ...

    def test_corrwith_series(self, datetime_frame: Any) -> None:
        ...

    def test_corrwith_matches_corrcoef(self) -> None:
        ...

    def test_corrwith_mixed_dtypes(self) -> None:
        ...

    def test_corrwith_index_intersection(self) -> None:
        ...

    def test_corrwith_index_union(self) -> None:
        ...

    def test_corrwith_dup_cols(self) -> None:
        ...

    def test_corrwith_spearman(self) -> None:
        ...

    def test_corrwith_kendall(self) -> None:
        ...

    def test_bool_describe_in_mixed_frame(self) -> None:
        ...

    def test_describe_empty_object(self) -> None:
        ...

    def test_describe_bool_frame(self) -> None:
        ...

    def test_describe_categorical(self) -> None:
        ...

    def test_describe_empty_categorical_column(self) -> None:
        ...

    def test_describe_categorical_columns(self) -> None:
        ...

    def test_describe_datetime_columns(self) -> None:
        ...

    def test_describe_timedelta_values(self) -> None:
        ...

    def test_describe_tz_values(self, tz_naive_fixture: Any) -> None:
        ...

    def test_describe_percentiles_integer_idx(self) -> None:
        ...

    def test_stat_op_api(
            self, float_frame: Any, float_string_frame: Any) -> None:
        ...

    def test_stat_op_calc(
            self, float_frame_with_na: Any, mixed_float_frame: Any) -> None:
        ...

    def test_median(self, float_frame_with_na: Any, int_frame: Any) -> None:
        ...

    def test_stat_operators_attempt_obj_array(self, method: Any) -> None:
        ...

    def test_mixed_ops(self, op: Any) -> None:
        ...

    def test_reduce_mixed_frame(self) -> None:
        ...

    def test_nunique(self) -> None:
        ...

    def test_mean_mixed_datetime_numeric(self, tz: Any) -> None:
        ...

    def test_mean_excludeds_datetimes(self, tz: Any) -> None:
        ...

    def test_var_std(self, datetime_frame: Any) -> None:
        ...

    def test_numeric_only_flag(self, meth: Any) -> None:
        ...

    def test_sem(self, datetime_frame: Any) -> None:
        ...

    def test_kurt(self) -> None:
        ...

    def test_mode_dropna(self, dropna: Any, expected: Any) -> None:
        ...

    def test_mode_sortwarning(self) -> None:
        ...

    def test_operators_timedelta64(self) -> None:
        ...

    def test_sum_corner(self) -> None:
        ...

    def test_sum_prod_nanops(self, method: Any, unit: Any) -> None:
        ...

    def test_sum_nanops_timedelta(self) -> None:
        ...

    def test_sum_object(self, float_frame: Any) -> None:
        ...

    def test_sum_bool(self, float_frame: Any) -> None:
        ...

    def test_mean_corner(
            self, float_frame: Any, float_string_frame: Any) -> None:
        ...

    def test_mean_datetimelike(self) -> None:
        ...

    def test_mean_datetimelike_numeric_only_false(self) -> None:
        ...

    def test_stats_mixed_type(self, float_string_frame: Any) -> None:
        ...

    def test_sum_bools(self) -> None:
        ...

    def test_cumsum_corner(self) -> None:
        ...

    def test_cumsum(self, datetime_frame: Any) -> None:
        ...

    def test_cumprod(self, datetime_frame: Any) -> None:
        ...

    def test_cummin(self, datetime_frame: Any) -> None:
        ...

    def test_cummax(self, datetime_frame: Any) -> None:
        ...

    def test_count(self) -> None:
        ...

    def test_count_objects(self, float_string_frame: Any) -> None:
        ...

    def test_pct_change(self) -> None:
        ...

    def test_idxmin(self, float_frame: Any, int_frame: Any) -> None:
        ...

    def test_idxmax(self, float_frame: Any, int_frame: Any) -> None:
        ...

    def test_any_all(
            self, opname: Any, bool_frame_with_na: Any,
            float_string_frame: Any) -> None:
        ...

    def test_any_all_extra(self) -> None:
        ...

    def test_any_datetime(self) -> None:
        ...

    def test_any_all_bool_only(self) -> None:
        ...

    def test_any_all_np_func(
            self, func: Any, data: Any, expected: Any) -> None:
        ...

    def test_any_all_object(self) -> None:
        ...

    def test_any_all_level_axis_none_raises(self, method: Any) -> None:
        ...

    def test_isin(self) -> None:
        ...

    def test_isin_empty(self, empty: Any) -> None:
        ...

    def test_isin_dict(self) -> None:
        ...

    def test_isin_with_string_scalar(self) -> None:
        ...

    def test_isin_df(self) -> None:
        ...

    def test_isin_tuples(self) -> None:
        ...

    def test_isin_df_dupe_values(self) -> None:
        ...

    def test_isin_dupe_self(self) -> None:
        ...

    def test_isin_against_series(self) -> None:
        ...

    def test_isin_multiIndex(self) -> None:
        ...

    def test_isin_empty_datetimelike(self) -> None:
        ...

    def test_round(self) -> None:
        ...

    def test_numpy_round(self) -> None:
        ...

    def test_numpy_round_nan(self) -> None:
        ...

    def test_round_mixed_type(self) -> None:
        ...

    def test_round_issue(self) -> None:
        ...

    def test_built_in_round(self) -> None:
        ...

    def test_round_nonunique_categorical(self) -> None:
        ...

    def test_clip(self, float_frame: Any) -> None:
        ...

    def test_inplace_clip(self, float_frame: Any) -> None:
        ...

    def test_dataframe_clip(self) -> None:
        ...

    def test_clip_mixed_numeric(self) -> None:
        ...

    def test_clip_against_series(self, inplace: Any) -> None:
        ...

    def test_clip_against_list_like(
            self, simple_frame: Any, inplace: Any, lower: Any, axis: Any,
            res: Any) -> None:
        ...

    def test_clip_against_frame(self, axis: Any) -> None:
        ...

    def test_clip_against_unordered_columns(self) -> None:
        ...

    def test_clip_with_na_args(self, float_frame: Any) -> None:
        ...

    def test_dot(self) -> None:
        ...

    def test_matmul(self) -> None:
        ...


def df_duplicates() -> Any:
    ...


def df_strings() -> Any:
    ...


def df_main_dtypes() -> Any:
    ...


class TestNLargestNSmallest:
    dtype_error_msg_template: str = ...

    def test_n(
            self, df_strings: Any, nselect_method: Any, n: Any,
            order: Any) -> None:
        ...

    def test_n_error(
            self, df_main_dtypes: Any, nselect_method: Any,
            columns: Any) -> None:
        ...

    def test_n_all_dtypes(self, df_main_dtypes: Any) -> None:
        ...

    def test_duplicates_on_starter_columns(
            self, method: Any, expected: Any) -> None:
        ...

    def test_n_identical_values(self) -> None:
        ...

    def test_n_duplicate_index(
            self, df_duplicates: Any, n: Any, order: Any) -> None:
        ...

    def test_duplicate_keep_all_ties(self) -> None:
        ...

    def test_series_broadcasting(self) -> None:
        ...

    def test_series_nat_conversion(self) -> None:
        ...

    def test_multiindex_column_lookup(self) -> None:
        ...
