# Stubs for pandas.tests.plotting.test_series (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any
from pandas.tests.plotting.common import TestPlotBase

class TestSeriesPlots(TestPlotBase):
    ts: Any = ...
    series: Any = ...
    iseries: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def test_plot(self) -> None:
        ...

    def test_plot_figsize_and_title(self) -> None:
        ...

    def test_dont_modify_rcParams(self) -> None:
        ...

    def test_ts_line_lim(self) -> None:
        ...

    def test_ts_area_lim(self) -> None:
        ...

    def test_label(self) -> None:
        ...

    def test_line_area_nan_series(self) -> None:
        ...

    def test_line_use_index_false(self) -> None:
        ...

    def test_bar_log(self) -> None:
        ...

    def test_bar_ignore_index(self) -> None:
        ...

    def test_bar_user_colors(self) -> None:
        ...

    def test_rotation(self) -> None:
        ...

    def test_irregular_datetime(self) -> None:
        ...

    def test_unsorted_index_xlim(self) -> None:
        ...

    def test_pie_series(self) -> None:
        ...

    def test_pie_nan(self) -> None:
        ...

    def test_hist_df_kwargs(self) -> None:
        ...

    def test_hist_df_with_nonnumerics(self) -> None:
        ...

    def test_hist_legacy(self) -> None:
        ...

    def test_hist_bins_legacy(self) -> None:
        ...

    def test_hist_layout(self) -> None:
        ...

    def test_hist_layout_with_by(self) -> None:
        ...

    def test_hist_no_overlap(self) -> None:
        ...

    def test_hist_secondary_legend(self) -> None:
        ...

    def test_df_series_secondary_legend(self) -> None:
        ...

    def test_secondary_logy(self, input_logy: Any, expected_scale: Any) -> None:
        ...

    def test_plot_fails_with_dupe_color_and_style(self) -> None:
        ...

    def test_hist_kde(self) -> None:
        ...

    def test_kde_kwargs(self) -> None:
        ...

    def test_kde_missing_vals(self) -> None:
        ...

    def test_hist_kwargs(self) -> None:
        ...

    def test_hist_kde_color(self) -> None:
        ...

    def test_boxplot_series(self) -> None:
        ...

    def test_kind_both_ways(self) -> None:
        ...

    def test_invalid_plot_data(self) -> None:
        ...

    def test_valid_object_plot(self) -> None:
        ...

    def test_partially_invalid_plot_data(self) -> None:
        ...

    def test_invalid_kind(self) -> None:
        ...

    def test_dup_datetime_index_plot(self) -> None:
        ...

    def test_errorbar_plot(self) -> None:
        ...

    def test_table(self) -> None:
        ...

    def test_series_grid_settings(self) -> None:
        ...

    def test_standard_colors(self) -> None:
        ...

    def test_standard_colors_all(self) -> None:
        ...

    def test_series_plot_color_kwargs(self) -> None:
        ...

    def test_time_series_plot_color_kwargs(self) -> None:
        ...

    def test_time_series_plot_color_with_empty_kwargs(self) -> None:
        ...

    def test_xticklabels(self) -> None:
        ...

    def test_custom_business_day_freq(self) -> None:
        ...

    def test_plot_accessor_updates_on_inplace(self) -> None:
        ...