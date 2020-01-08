# Stubs for pandas.tests.indexes.test_base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,arguments-differ

from typing import Any
from pandas.tests.indexes.common import Base

class TestIndex(Base):
    indices: Any = ...

    def setup_method(self, method: Any) -> None:
        ...

    def create_index(self):
        ...

    def generate_index_types(self, skip_index_keys: Any = ...) -> None:
        ...

    def test_can_hold_identifiers(self) -> None:
        ...

    def test_new_axis(self) -> None:
        ...

    def test_copy_and_deepcopy(self) -> None:
        ...

    def test_constructor_regular(self, attr: Any) -> None:
        ...

    def test_constructor_casting(self) -> None:
        ...

    def test_constructor_copy(self) -> None:
        ...

    def test_constructor_corner(self) -> None:
        ...

    def test_construction_list_mixed_tuples(self, index_vals: Any) -> None:
        ...

    def test_construction_list_tuples_nan(
            self, na_value: Any, vtype: Any) -> None:
        ...

    def test_constructor_from_index_dtlike(
            self, cast_as_obj: Any, index: Any) -> None:
        ...

    def test_constructor_from_series_dtlike(
            self, index: Any, has_tz: Any) -> None:
        ...

    def test_constructor_from_series(self, klass: Any) -> None:
        ...

    def test_constructor_from_series_freq(self) -> None:
        ...

    def test_constructor_from_frame_series_freq(self) -> None:
        ...

    array: Any = ...

    def test_constructor_ndarray_like(self, array: Any) -> None:
        ...

    def test_constructor_int_dtype_float(self, dtype: Any) -> None:
        ...

    def test_constructor_int_dtype_nan(self) -> None:
        ...

    def test_constructor_int_dtype_nan_raises(self, dtype: Any) -> None:
        ...

    def test_constructor_no_pandas_array(self) -> None:
        ...

    def test_index_ctor_infer_nan_nat(
            self, klass: Any, dtype: Any, na_val: Any) -> None:
        ...

    def test_index_ctor_infer_nat_dt_like(
            self, pos: Any, klass: Any, dtype: Any, ctor: Any,
            nulls_fixture: Any) -> None:
        ...

    def test_index_ctor_nat_result(self, swap_objs: Any) -> None:
        ...

    def test_index_ctor_infer_periodindex(self) -> None:
        ...

    def test_constructor_simple_new(self, vals: Any, dtype: Any) -> None:
        ...

    def test_constructor_dtypes_to_int64(self, vals: Any) -> None:
        ...

    def test_constructor_dtypes_to_float64(self, vals: Any) -> None:
        ...

    def test_constructor_dtypes_to_object(
            self, cast_index: Any, vals: Any) -> None:
        ...

    def test_constructor_dtypes_to_categorical(self, vals: Any) -> None:
        ...

    def test_constructor_dtypes_to_datetime(
            self, cast_index: Any, vals: Any) -> None:
        ...

    def test_constructor_dtypes_to_timedelta(
            self, cast_index: Any, vals: Any) -> None:
        ...

    def test_constructor_dtypes_datetime(
            self, tz_naive_fixture: Any, attr: Any, utc: Any,
            klass: Any) -> None:
        ...

    def test_constructor_dtypes_timedelta(self, attr: Any, klass: Any) -> None:
        ...

    def test_constructor_empty(self, value: Any, klass: Any) -> None:
        ...

    def test_constructor_empty_special(self, empty: Any, klass: Any) -> None:
        ...

    def test_constructor_overflow_int64(self) -> None:
        ...

    def test_constructor_cast(self) -> None:
        ...

    def test_view_with_args(self) -> None:
        ...

    def test_view_with_args_object_array_raises(self, index_type: Any) -> None:
        ...

    def test_astype(self) -> None:
        ...

    def test_equals_object(self) -> None:
        ...

    def test_not_equals_object(self, comp: Any) -> None:
        ...

    def test_insert(self) -> None:
        ...

    def test_insert_missing(self, nulls_fixture: Any) -> None:
        ...

    def test_delete(self, pos: Any, expected: Any) -> None:
        ...

    def test_delete_raises(self) -> None:
        ...

    def test_identical(self) -> None:
        ...

    def test_is_(self) -> None:
        ...

    def test_asof(self) -> None:
        ...

    def test_asof_datetime_partial(self) -> None:
        ...

    def test_nanosecond_index_access(self) -> None:
        ...

    def test_booleanindex(self) -> None:
        ...

    def test_fancy(self) -> None:
        ...

    def test_empty_fancy(self, attr: Any, dtype: Any) -> None:
        ...

    def test_empty_fancy_raises(self, attr: Any) -> None:
        ...

    def test_intersection(self, sort: Any) -> None:
        ...

    def test_intersection_name_preservation(
            self, index2: Any, keeps_name: Any, sort: Any) -> None:
        ...

    def test_intersection_name_preservation2(
            self, first_name: Any, second_name: Any, expected_name: Any,
            sort: Any) -> None:
        ...

    def test_intersection_monotonic(
            self, index2: Any, keeps_name: Any, sort: Any) -> None:
        ...

    def test_intersection_non_monotonic_non_unique(
            self, index2: Any, expected_arr: Any, sort: Any) -> None:
        ...

    def test_intersect_str_dates(self, sort: Any) -> None:
        ...

    def test_intersect_nosort(self) -> None:
        ...

    def test_intersection_equal_sort(self) -> None:
        ...

    def test_intersection_equal_sort_true(self) -> None:
        ...

    def test_chained_union(self, sort: Any) -> None:
        ...

    def test_union(self, sort: Any) -> None:
        ...

    def test_union_sort_other_special(self, slice_: Any) -> None:
        ...

    def test_union_sort_special_true(self, slice_: Any) -> None:
        ...

    def test_union_sort_other_incomparable(self) -> None:
        ...

    def test_union_sort_other_incomparable_true(self) -> None:
        ...

    def test_union_from_iterables(self, klass: Any, sort: Any) -> None:
        ...

    def test_union_identity(self, sort: Any) -> None:
        ...

    def test_union_name_preservation(
            self, first_list: Any, second_list: Any, first_name: Any,
            second_name: Any, expected_name: Any, sort: Any) -> None:
        ...

    def test_union_dt_as_obj(self, sort: Any) -> None:
        ...

    def test_setops_disallow_true(self, method: Any) -> None:
        ...

    def test_map_identity_mapping(self):
        ...

    def test_map_with_tuples(self):
        ...

    def test_map_with_tuples_mi(self):
        ...

    def test_map_tseries_indices_return_index(self, attr: Any) -> None:
        ...

    def test_map_tseries_indices_accsr_return_index(self):
        ...

    def test_map_dictlike(self, mapper: Any) -> None:
        ...

    def test_map_with_non_function_missing_values(self, mapper: Any) -> None:
        ...

    def test_map_na_exclusion(self):
        ...

    def test_map_defaultdict(self):
        ...

    def test_append_multiple(self) -> None:
        ...

    def test_append_empty_preserve_name(self, name: Any, expected: Any) -> None:
        ...

    def test_difference_name_preservation(
            self, second_name: Any, expected: Any, sort: Any) -> None:
        ...

    def test_difference_empty_arg(self, sort: Any) -> None:
        ...

    def test_difference_identity(self, sort: Any) -> None:
        ...

    def test_difference_sort(self, sort: Any) -> None:
        ...

    def test_symmetric_difference(self, sort: Any) -> None:  # type: ignore
        ...

    def test_difference_incomparable(self, opname: Any) -> None:
        ...

    def test_difference_incomparable_true(self, opname: Any) -> None:
        ...

    def test_symmetric_difference_mi(self, sort: Any) -> None:
        ...

    def test_symmetric_difference_missing(
            self, index2: Any, expected: Any, sort: Any) -> None:
        ...

    def test_symmetric_difference_non_index(self, sort: Any) -> None:
        ...

    def test_difference_type(self, sort: Any) -> None:
        ...

    def test_intersection_difference(self, sort: Any) -> None:
        ...

    def test_is_numeric(self, attr: Any, expected: Any) -> None:
        ...

    def test_is_object(self, attr: Any, expected: Any) -> None:
        ...

    def test_is_all_dates(self, attr: Any, expected: Any) -> None:
        ...

    def test_summary(self) -> None:
        ...

    def test_summary_deprecated(self) -> None:
        ...

    def test_format(self) -> None:
        ...

    def test_format_missing(self, vals: Any, nulls_fixture: Any) -> None:
        ...

    def test_format_with_name_time_info(self) -> None:
        ...

    def test_format_datetime_with_time(self) -> None:
        ...

    def test_logical_compat(self, op: Any) -> None:  # type: ignore
        ...

    def test_get_indexer(self) -> None:
        ...

    def test_get_indexer_methods(
            self, reverse: Any, expected: Any, method: Any) -> None:
        ...

    def test_get_indexer_invalid(self) -> None:
        ...

    def test_get_indexer_nearest(
            self, method: Any, tolerance: Any, indexer: Any,
            expected: Any) -> None:
        ...

    def test_get_indexer_nearest_listlike_tolerance(
            self, tolerance: Any, expected: Any, listtype: Any) -> None:
        ...

    def test_get_indexer_nearest_error(self) -> None:
        ...

    def test_get_indexer_nearest_decreasing(
            self, method: Any, expected: Any) -> None:
        ...

    def test_get_indexer_strings(self, method: Any, expected: Any) -> None:
        ...

    def test_get_indexer_strings_raises(self) -> None:
        ...

    def test_get_indexer_numeric_index_boolean_target(
            self, idx_class: Any) -> None:
        ...

    def test_get_indexer_with_NA_values(
            self, unique_nulls_fixture: Any,
            unique_nulls_fixture2: Any) -> None:
        ...

    def test_get_loc(self, method: Any) -> None:
        ...

    def test_get_loc_raises_bad_label(self, method: Any) -> None:
        ...

    def test_get_loc_tolerance(self, method: Any, loc: Any) -> None:
        ...

    def test_get_loc_outside_tolerance_raises(self, method: Any) -> None:
        ...

    def test_get_loc_bad_tolerance_raises(self) -> None:
        ...

    def test_get_loc_tolerance_no_method_raises(self) -> None:
        ...

    def test_get_loc_raises_missized_tolerance(self) -> None:
        ...

    def test_get_loc_raises_object_nearest(self) -> None:
        ...

    def test_get_loc_raises_object_tolerance(self) -> None:
        ...

    def test_slice_locs(self, dtype: Any) -> None:
        ...

    def test_slice_float_locs(self, dtype: Any) -> None:
        ...

    def test_slice_locs_dup(self) -> None:
        ...

    def test_slice_locs_dup_numeric(self, dtype: Any) -> None:
        ...

    def test_slice_locs_na(self) -> None:
        ...

    def test_slice_locs_na_raises(self) -> None:
        ...

    def test_slice_locs_negative_step(
            self, in_slice: Any, expected: Any) -> None:
        ...

    def test_drop_by_str_label(self) -> None:
        ...

    def test_drop_by_str_label_raises_missing_keys(self, keys: Any) -> None:
        ...

    def test_drop_by_str_label_errors_ignore(self) -> None:
        ...

    def test_drop_by_numeric_label_loc(self) -> None:
        ...

    def test_drop_by_numeric_label_raises_missing_keys(self) -> None:
        ...

    def test_drop_by_numeric_label_errors_ignore(
            self, key: Any, expected: Any) -> None:
        ...

    def test_drop_tuple(self, values: Any, to_drop: Any) -> None:
        ...

    def test_tuple_union_bug(
            self, method: Any, expected: Any, sort: Any) -> None:
        ...

    def test_is_monotonic_incomparable(self, attr: Any) -> None:
        ...

    def test_get_set_value(self) -> None:
        ...

    def test_isin(self, values: Any, index: Any, expected: Any) -> None:
        ...

    def test_isin_nan_common_object(
            self, nulls_fixture: Any, nulls_fixture2: Any) -> None:
        ...

    def test_isin_nan_common_float64(self, nulls_fixture: Any) -> None:
        ...

    def test_isin_level_kwarg(self, level: Any, index: Any) -> None:
        ...

    def test_isin_level_kwarg_bad_level_raises(
            self, level: Any, indices: Any) -> None:
        ...

    def test_isin_level_kwarg_bad_label_raises(
            self, label: Any, indices: Any) -> None:
        ...

    def test_isin_empty(self, empty: Any) -> None:
        ...

    def test_boolean_cmp(self, values: Any) -> None:
        ...

    def test_get_level_values(self, name: Any, level: Any) -> None:
        ...

    def test_slice_keep_name(self) -> None:
        ...

    def test_join_self(self, join_type: Any, index_kind: Any) -> None:
        ...

    def test_str_attribute(self, method: Any) -> None:
        ...

    def test_str_attribute_raises(self, index: Any) -> None:
        ...

    def test_str_split(self, expand: Any, expected: Any) -> None:
        ...

    def test_str_bool_return(self) -> None:
        ...

    def test_str_bool_series_indexing(self) -> None:
        ...

    def test_tab_completion(self, index: Any, expected: Any) -> None:
        ...

    def test_indexing_doesnt_change_class(self) -> None:
        ...

    def test_outer_join_sort(self) -> None:
        ...

    def test_nan_first_take_datetime(self) -> None:
        ...

    def test_take_fill_value(self) -> None:
        ...

    def test_take_fill_value_none_raises(self) -> None:
        ...

    def test_take_bad_bounds_raises(self) -> None:
        ...

    def test_reindex_preserves_name_if_target_is_list_or_ndarray(
            self, name: Any, labels: Any) -> None:
        ...

    def test_reindex_preserves_type_if_target_is_empty_list_or_array(
            self, labels: Any) -> None:
        ...

    def test_reindex_doesnt_preserve_type_if_target_is_empty_index(
            self, labels: Any, dtype: Any) -> None:
        ...

    def test_reindex_no_type_preserve_target_empty_mi(self) -> None:
        ...

    def test_groupby(self) -> None:
        ...

    def test_equals_op_multiindex(self, mi: Any, expected: Any) -> None:
        ...

    def test_equals_op_multiindex_identify(self) -> None:
        ...

    def test_equals_op_mismatched_multiindex_raises(self, index: Any) -> None:
        ...

    def test_equals_op_index_vs_mi_same_length(self) -> None:
        ...

    def test_dt_conversion_preserves_name(self, dt_conv: Any) -> None:
        ...

    def test_string_index_repr(self, index: Any, expected: Any) -> None:
        ...

    def test_string_index_repr_with_unicode_option(
            self, index: Any, expected: Any) -> None:
        ...

    def test_cached_properties_not_settable(self) -> None:
        ...

    def test_get_duplicates_deprecated(self) -> None:
        ...

    def test_tab_complete_warning(self, ip: Any) -> None:
        ...

    def test_deprecated_contains(self) -> None:
        ...


class TestMixedIntIndex(Base):
    indices: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def create_index(self):
        ...

    def test_argsort(self) -> None:
        ...

    def test_numpy_argsort(self) -> None:
        ...

    def test_copy_name(self) -> None:
        ...

    def test_copy_name2(self) -> None:
        ...

    def test_union_base(self) -> None:
        ...

    def test_union_different_type_base(self, klass: Any) -> None:
        ...

    def test_unique_na(self) -> None:
        ...

    def test_intersection_base(self, sort: Any) -> None:  # type: ignore
        ...

    def test_intersection_different_type_base(
            self, klass: Any, sort: Any) -> None:
        ...

    def test_difference_base(self, sort: Any) -> None:
        ...

    def test_symmetric_difference(self) -> None:
        ...

    def test_logical_compat(self) -> None:
        ...

    def test_dropna(
            self, how: Any, dtype: Any, vals: Any, expected: Any) -> None:
        ...

    def test_dropna_dt_like(
            self, how: Any, index: Any, expected: Any) -> None:
        ...

    def test_dropna_invalid_how_raises(self) -> None:
        ...

    def test_get_combined_index(self) -> None:
        ...

    def test_repeat(self) -> None:
        ...

    def test_is_monotonic_na(self, index: Any) -> None:
        ...

    def test_repr_summary(self) -> None:
        ...

    def test_int_name_format(self, klass: Any) -> None:
        ...

    def test_print_unicode_columns(self) -> None:
        ...

    def test_str_to_bytes_raises(self) -> None:
        ...

    def test_intersect_str_dates(self) -> None:
        ...


class TestIndexUtils:
    def test_ensure_index_from_sequences(
            self, data: Any, names: Any, expected: Any) -> None:
        ...

    def test_ensure_index_mixed_closed_intervals(self) -> None:
        ...


def test_generated_op_names(opname: Any, indices: Any) -> None:
    ...


def test_index_subclass_constructor_wrong_kwargs(index_maker: Any) -> None:
    ...


def test_deprecated_fastpath() -> None:
    ...