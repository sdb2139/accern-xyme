# Stubs for pandas.tests.groupby.test_grouping (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any


class TestSelection:
    def test_select_bad_cols(self) -> None:
        ...

    def test_groupby_duplicated_column_errormsg(self) -> None:
        ...

    def test_column_select_via_attr(self, df: Any) -> None:
        ...

    def test_getitem_list_of_columns(self) -> None:
        ...

    def test_getitem_numeric_column_names(self) -> None:
        ...


class TestGrouping:
    def test_grouper_index_types(self):
        ...

    def test_grouper_multilevel_freq(self) -> None:
        ...

    def test_grouper_creation_bug(self):
        ...

    def test_grouper_column_and_index(self) -> None:
        ...

    def test_groupby_levels_and_columns(self) -> None:
        ...

    def test_groupby_categorical_index_and_columns(
            self, observed: Any) -> None:
        ...

    def test_grouper_getting_correct_binner(self) -> None:
        ...

    def test_grouper_iter(self, df: Any) -> None:
        ...

    def test_empty_groups(self, df: Any) -> None:
        ...

    def test_groupby_grouper(self, df: Any) -> None:
        ...

    def test_groupby_dict_mapping(self) -> None:
        ...

    def test_groupby_grouper_f_sanity_checked(self):
        ...

    def test_grouping_error_on_multidim_input(self, df: Any) -> None:
        ...

    def test_multiindex_passthru(self) -> None:
        ...

    def test_multiindex_negative_level(self, mframe: Any) -> None:
        ...

    def test_multifunc_select_col_integer_cols(self, df: Any) -> None:
        ...

    def test_multiindex_columns_empty_level(self) -> None:
        ...

    def test_groupby_multiindex_tuple(self) -> None:
        ...

    def test_groupby_level(self, sort: Any, mframe: Any, df: Any) -> None:
        ...

    def test_groupby_level_index_names(self) -> None:
        ...

    def test_groupby_level_with_nas(self, sort: Any) -> None:
        ...

    def test_groupby_args(self, mframe: Any) -> None:
        ...

    def test_level_preserve_order(
            self, sort: Any, labels: Any, mframe: Any) -> None:
        ...

    def test_grouping_labels(self, mframe: Any) -> None:
        ...

    def test_list_grouper_with_nat(self) -> None:
        ...

    def test_evaluate_with_empty_groups(
            self, func: Any, expected: Any) -> None:
        ...

    def test_groupby_empty(self) -> None:
        ...


class TestGetGroup:
    def test_get_group(self) -> None:
        ...

    def test_get_group_empty_bins(self, observed: Any) -> None:
        ...

    def test_get_group_grouped_by_tuple(self) -> None:
        ...

    def test_groupby_with_empty(self) -> None:
        ...

    def test_groupby_with_single_column(self) -> None:
        ...

    def test_gb_key_len_equal_axis_len(self) -> None:
        ...


class TestIteration:
    def test_groups(self, df: Any) -> None:
        ...

    def test_grouping_is_iterable(self, tsframe: Any) -> None:
        ...

    def test_multi_iter(self) -> None:
        ...

    def test_multi_iter_frame(self, three_group: Any) -> None:
        ...

    def test_dictify(self, df: Any) -> None:
        ...

    def test_groupby_with_small_elem(self) -> None:
        ...

    def test_grouping_string_repr(self) -> None:
        ...
