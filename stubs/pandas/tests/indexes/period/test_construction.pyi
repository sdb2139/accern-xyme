# Stubs for pandas.tests.indexes.period.test_construction (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ

from typing import Any


class TestPeriodIndex:
    def setup_method(self, method: Any) -> None:
        ...

    def test_construction_base_constructor(self) -> None:
        ...

    def test_constructor_use_start_freq(self) -> None:
        ...

    def test_constructor_field_arrays(self) -> None:
        ...

    def test_constructor_U(self) -> None:
        ...

    def test_constructor_nano(self) -> None:
        ...

    def test_constructor_arrays_negative_year(self) -> None:
        ...

    def test_constructor_invalid_quarters(self) -> None:
        ...

    def test_constructor_corner(self) -> None:
        ...

    def test_constructor_fromarraylike(self) -> None:
        ...

    def test_constructor_datetime64arr(self) -> None:
        ...

    def test_constructor_datetime64arr_ok(self, box: Any) -> None:
        ...

    def test_constructor_dtype(self) -> None:
        ...

    def test_constructor_empty(self) -> None:
        ...

    def test_constructor_pi_nat(self) -> None:
        ...

    def test_constructor_incompat_freq(self) -> None:
        ...

    def test_constructor_mixed(self) -> None:
        ...

    def test_constructor_simple_new(self) -> None:
        ...

    def test_constructor_simple_new_empty(self) -> None:
        ...

    def test_constructor_floats(self, floats: Any) -> None:
        ...

    def test_constructor_nat(self) -> None:
        ...

    def test_constructor_year_and_quarter(self) -> None:
        ...

    def test_constructor_freq_mult(self, func: Any, warning: Any) -> None:
        ...

    def test_constructor_freq_mult_dti_compat(self, mult: Any, freq: Any) -> None:
        ...

    def test_constructor_freq_combined(self) -> None:
        ...

    def test_constructor_range_based_deprecated(self) -> None:
        ...

    def test_constructor_range_based_deprecated_different_freq(self) -> None:
        ...

    def test_constructor(self) -> None:
        ...

    def test_constructor_error(self) -> None:
        ...

    def test_recreate_from_data(self, freq: Any) -> None:
        ...

    def test_map_with_string_constructor(self) -> None:
        ...


class TestSeriesPeriod:
    series: Any = ...
    def setup_method(self, method: Any) -> None:
        ...

    def test_constructor_cant_cast_period(self) -> None:
        ...

    def test_constructor_cast_object(self) -> None:
        ...
