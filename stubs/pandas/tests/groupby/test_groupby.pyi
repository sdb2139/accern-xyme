# Stubs for pandas.tests.groupby.test_groupby (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any


def test_repr() -> None:
    ...


def test_basic(dtype: Any) -> None:
    ...


def test_groupby_nonobject_dtype(mframe: Any, df_mixed_floats: Any) -> None:
    ...


def test_groupby_return_type() -> None:
    ...


def test_inconsistent_return_type() -> None:
    ...


def test_pass_args_kwargs(ts: Any, tsframe: Any) -> None:
    ...


def test_len() -> None:
    ...


def test_basic_regression() -> None:
    ...


def test_with_na_groups(dtype: Any) -> None:
    ...


def test_indices_concatenation_order() -> None:
    ...


def test_attr_wrapper(ts: Any) -> None:
    ...


def test_frame_groupby(tsframe: Any) -> None:
    ...


def test_frame_groupby_columns(tsframe: Any) -> None:
    ...


def test_frame_set_name_single(df: Any) -> None:
    ...


def test_multi_func(df: Any) -> None:
    ...


def test_multi_key_multiple_functions(df: Any) -> None:
    ...


def test_frame_multi_key_function_list() -> None:
    ...


def test_groupby_multiple_columns(df: Any, op: Any) -> None:
    ...


def test_groupby_as_index_agg(df: Any) -> None:
    ...


def test_as_index_series_return_frame(df: Any) -> None:
    ...


def test_as_index_series_column_slice_raises(df: Any) -> None:
    ...


def test_groupby_as_index_cython(df: Any) -> None:
    ...


def test_groupby_as_index_series_scalar(df: Any) -> None:
    ...


def test_groupby_as_index_corner(df: Any, ts: Any) -> None:
    ...


def test_groupby_multiple_key(df: Any) -> None:
    ...


def test_groupby_multi_corner(df: Any) -> None:
    ...


def test_omit_nuisance(df: Any) -> None:
    ...


def test_omit_nuisance_python_multiple(three_group: Any) -> None:
    ...


def test_empty_groups_corner(mframe: Any) -> None:
    ...


def test_nonsense_func() -> None:
    ...


def test_wrap_aggregated_output_multindex(mframe: Any) -> None:
    ...


def test_groupby_level_apply(mframe: Any) -> None:
    ...


def test_groupby_level_mapper(mframe: Any) -> None:
    ...


def test_groupby_level_nonmulti() -> None:
    ...


def test_groupby_complex() -> None:
    ...


def test_mutate_groups() -> None:
    ...


def test_no_mutate_but_looks_like() -> None:
    ...


def test_groupby_series_indexed_differently() -> None:
    ...


def test_groupby_with_hier_columns() -> None:
    ...


def test_grouping_ndarray(df: Any) -> None:
    ...


def test_groupby_wrong_multi_labels() -> None:
    ...


def test_groupby_series_with_name(df: Any) -> None:
    ...


def test_seriesgroupby_name_attr(df: Any) -> None:
    ...


def test_consistency_name() -> None:
    ...


def test_groupby_name_propagation(df: Any) -> None:
    ...


def test_groupby_nonstring_columns() -> None:
    ...


def test_groupby_mixed_type_columns() -> None:
    ...


def test_cython_grouper_series_bug_noncontig() -> None:
    ...


def test_series_grouper_noncontig_index() -> None:
    ...


def test_convert_objects_leave_decimal_alone() -> None:
    ...


def test_groupby_dtype_inference_empty() -> None:
    ...


def test_groupby_list_infer_array_like(df: Any) -> None:
    ...


def test_groupby_keys_same_size_as_index() -> None:
    ...


def test_groupby_one_row() -> None:
    ...


def test_groupby_nat_exclude() -> None:
    ...


def test_groupby_2d_malformed() -> None:
    ...


def test_int32_overflow() -> None:
    ...


def test_groupby_sort_multi() -> None:
    ...


def test_dont_clobber_name_column() -> None:
    ...


def test_skip_group_keys() -> None:
    ...


def test_no_nonsense_name(float_frame: Any) -> None:
    ...


def test_multifunc_sum_bug() -> None:
    ...


def test_handle_dict_return_value(df: Any) -> None:
    ...


def test_set_group_name(df: Any, grouper: Any) -> None:
    ...


def test_group_name_available_in_inference_pass() -> None:
    ...


def test_no_dummy_key_names(df: Any) -> None:
    ...


def test_groupby_sort_multiindex_series() -> None:
    ...


def test_groupby_reindex_inside_function() -> None:
    ...


def test_groupby_multiindex_missing_pair() -> None:
    ...


def test_groupby_multiindex_not_lexsorted() -> None:
    ...


def test_index_label_overlaps_location() -> None:
    ...


def test_transform_doesnt_clobber_ints() -> None:
    ...


def test_groupby_preserves_sort(sort_column: Any, group_column: Any) -> None:
    ...


def test_group_shift_with_null_key() -> None:
    ...


def test_group_shift_with_fill_value() -> None:
    ...


def test_pivot_table_values_key_error() -> None:
    ...


def test_empty_dataframe_groupby() -> None:
    ...


def test_tuple_warns() -> None:
    ...


def test_tuple_warns_unhashable() -> None:
    ...


def test_tuple_correct_keyerror() -> None:
    ...


def test_groupby_agg_ohlc_non_first() -> None:
    ...


def test_groupby_multiindex_nat() -> None:
    ...


def test_groupby_empty_list_raises() -> None:
    ...


def test_groupby_multiindex_series_keys_len_equal_group_axis() -> None:
    ...


def test_groupby_groups_in_BaseGrouper() -> None:
    ...
