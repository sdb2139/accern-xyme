# Stubs for pandas.tests.generic.test_series (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level


from typing import Any
from .test_generic import Generic

class TestSeries(Generic):
    ts: Any = ...
    series: Any = ...

    def setup_method(self) -> None:
        ...

    def test_rename_mi(self) -> None:
        ...

    def test_set_axis_name(self) -> None:
        ...

    def test_set_axis_name_mi(self) -> None:
        ...

    def test_set_axis_name_raises(self) -> None:
        ...

    def test_get_numeric_data_preserve_dtype(self) -> None:
        ...

    def test_nonzero_single_element(self) -> None:
        ...

    def test_metadata_propagation_indiv(self):
        ...

    def test_to_xarray_index_types(self, index: Any) -> None:
        ...

    def test_to_xarray(self) -> None:
        ...

    def test_valid_deprecated(self) -> None:
        ...

    def test_shift_always_copy(self, s: Any, shift_size: Any) -> None:
        ...

    def test_datetime_shift_always_copy(self, move_by_freq: Any) -> None:
        ...
