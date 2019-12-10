# Stubs for pandas.tests.frame.test_convert_to (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any
from pandas.tests.frame.common import TestData

class TestDataFrameConvertTo(TestData):
    def test_to_dict_timestamp(self) -> None:
        ...

    def test_to_dict_index_not_unique_with_index_orient(self) -> None:
        ...

    def test_to_dict_invalid_orient(self) -> None:
        ...

    def test_to_records_dt64(self) -> None:
        ...

    def test_to_records_with_multindex(self) -> None:
        ...

    def test_to_records_with_Mapping_type(self) -> None:
        ...

    def test_to_records_floats(self) -> None:
        ...

    def test_to_records_index_name(self) -> None:
        ...

    def test_to_records_with_unicode_index(self) -> None:
        ...

    def test_to_records_with_unicode_column_names(self) -> None:
        ...

    def test_to_records_with_categorical(self) -> None:
        ...

    def test_to_records_dtype(self, kwargs: Any, expected: Any) -> None:
        ...

    def test_to_records_dtype_mi(
            self, df: Any, kwargs: Any, expected: Any) -> None:
        ...

    d: Any = ...

    def test_to_records_dict_like(self):
        ...

    def test_to_dict(self, mapping: Any) -> None:
        ...

    def test_to_dict_errors(self, mapping: Any) -> None:
        ...

    def test_to_dict_not_unique_warning(self) -> None:
        ...

    def test_to_records_datetimeindex_with_tz(self, tz: Any) -> None:
        ...

    def test_to_dict_box_scalars(self, orient: Any, item_getter: Any) -> None:
        ...

    def test_frame_to_dict_tz(self) -> None:
        ...

    def test_to_dict_index_dtypes(self, into: Any, expected: Any) -> None:
        ...

    def test_to_dict_numeric_names(self) -> None:
        ...

    def test_to_dict_wide(self) -> None:
        ...
