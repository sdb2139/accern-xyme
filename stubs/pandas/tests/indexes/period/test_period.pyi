# Stubs for pandas.tests.indexes.period.test_period (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ

from typing import Any
from ..datetimelike import DatetimeLike

class TestPeriodIndex(DatetimeLike):
    indices: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def create_index(self):
        ...

    def test_pickle_compat_construction(self) -> None:
        ...

    def test_pickle_round_trip(self, freq: Any) -> None:
        ...

    def test_where(self) -> None:  # type: ignore
        ...

    def test_repeat_freqstr(self, index: Any, use_numpy: Any) -> None:
        ...

    def test_fillna_period(self) -> None:
        ...

    def test_no_millisecond_field(self) -> None:
        ...

    def test_difference_freq(self, sort: Any) -> None:
        ...

    def test_hash_error(self) -> None:
        ...

    def test_make_time_series(self) -> None:
        ...

    def test_shallow_copy_empty(self) -> None:
        ...

    def test_shallow_copy_i8(self) -> None:
        ...

    def test_shallow_copy_changing_freq_raises(self) -> None:
        ...

    def test_dtype_str(self) -> None:
        ...

    def test_view_asi8(self) -> None:
        ...

    def test_values(self) -> None:
        ...

    def test_period_index_length(self) -> None:
        ...

    def test_fields(self) -> None:
        ...

    def test_period_set_index_reindex(self) -> None:
        ...

    def test_factorize(self) -> None:
        ...

    def test_is_(self):
        ...

    def test_contains(self) -> None:
        ...

    def test_contains_nat(self) -> None:
        ...

    def test_periods_number_check(self) -> None:
        ...

    def test_start_time(self) -> None:
        ...

    def test_end_time(self) -> None:
        ...

    def test_index_duplicate_periods(self) -> None:
        ...

    def test_index_unique(self) -> None:
        ...

    def test_shift(self) -> None:
        ...

    def test_ndarray_compat_properties(self) -> None:
        ...

    def test_negative_ordinals(self) -> None:
        ...

    def test_pindex_fieldaccessor_nat(self) -> None:
        ...

    def test_pindex_qaccess(self) -> None:
        ...

    def test_pindex_multiples(self) -> None:
        ...

    def test_iteration(self) -> None:
        ...

    def test_is_full(self) -> None:
        ...

    def test_with_multi_index(self) -> None:
        ...

    def test_convert_array_of_periods(self) -> None:
        ...

    def test_append_concat(self) -> None:
        ...

    def test_pickle_freq(self) -> None:
        ...

    def test_map(self):
        ...

    def test_join_self(self, join_type: Any) -> None:
        ...

    def test_insert(self) -> None:
        ...


def test_maybe_convert_timedelta() -> None:
    ...