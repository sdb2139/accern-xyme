# Stubs for pandas.tests.series.test_timeseries (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any
from pandas.tests.series.common import TestData

def assert_range_equal(left: Any, right: Any) -> None:
    ...


class TestTimeSeries(TestData):
    def test_shift(self) -> None:
        ...

    def test_shift2(self) -> None:
        ...

    def test_shift_fill_value(self) -> None:
        ...

    def test_categorical_shift_fill_value(self) -> None:
        ...

    def test_shift_dst(self) -> None:
        ...

    def test_tshift(self) -> None:
        ...

    def test_truncate(self) -> None:
        ...

    def test_truncate_nonsortedindex(self) -> None:
        ...

    def test_asfreq(self) -> None:
        ...

    def test_asfreq_datetimeindex_empty_series(self) -> None:
        ...

    def test_diff(self) -> None:
        ...

    def test_pct_change(self) -> None:
        ...

    def test_pct_change_shift_over_nas(self) -> None:
        ...

    def test_pct_change_periods_freq(self, freq: Any, periods: Any, fill_method: Any, limit: Any) -> None:
        ...

    def test_autocorr(self) -> None:
        ...

    def test_first_last_valid(self) -> None:
        ...

    def test_mpl_compat_hack(self) -> None:
        ...

    def test_timeseries_coercion(self) -> None:
        ...

    def test_contiguous_boolean_preserve_freq(self) -> None:
        ...

    def test_to_datetime_unit(self) -> None:
        ...

    def test_series_ctor_datetime64(self) -> None:
        ...

    def test_series_repr_nat(self) -> None:
        ...

    def test_asfreq_keep_index_name(self) -> None:
        ...

    def test_promote_datetime_date(self) -> None:
        ...

    def test_asfreq_normalize(self) -> None:
        ...

    def test_first_subset(self) -> None:
        ...

    def test_first_raises(self) -> None:
        ...

    def test_last_subset(self) -> None:
        ...

    def test_last_raises(self) -> None:
        ...

    def test_format_pre_1900_dates(self) -> None:
        ...

    def test_at_time(self) -> None:
        ...

    def test_at_time_raises(self) -> None:
        ...

    def test_between(self) -> None:
        ...

    def test_between_time(self) -> None:
        ...

    def test_between_time_raises(self) -> None:
        ...

    def test_between_time_types(self) -> None:
        ...

    def test_between_time_formats(self) -> None:
        ...

    def test_between_time_axis(self) -> None:
        ...

    def test_to_period(self) -> None:
        ...

    def test_groupby_count_dateparseerror(self):
        ...

    def test_to_csv_numpy_16_bug(self) -> None:
        ...

    def test_series_map_box_timedelta(self):
        ...

    def test_asfreq_resample_set_correct_freq(self) -> None:
        ...

    def test_pickle(self) -> None:
        ...

    def test_setops_preserve_freq(self, tz: Any) -> None:
        ...

    def test_from_M8_structured(self) -> None:
        ...

    def test_get_level_values_box(self) -> None:
        ...

    def test_view_tz(self) -> None:
        ...

    def test_asarray_tz_naive(self) -> None:
        ...

    def test_asarray_tz_aware(self) -> None:
        ...