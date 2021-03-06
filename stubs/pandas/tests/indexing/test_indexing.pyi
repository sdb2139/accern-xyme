# Stubs for pandas.tests.indexing.test_indexing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,too-many-ancestors

from typing import Any
from pandas.tests.indexing.common import Base

ignore_ix: Any

class TestFancy(Base):
    def test_setitem_ndarray_1d(self) -> None:
        ...

    def test_getitem_ndarray_3d(self, index: Any, obj: Any, idxr: Any, idxr_id: Any) -> None:
        ...

    def test_setitem_ndarray_3d(self, index: Any, obj: Any, idxr: Any, idxr_id: Any) -> None:
        ...

    def test_inf_upcast(self) -> None:
        ...

    def test_setitem_dtype_upcast(self) -> None:
        ...

    def test_dups_fancy_indexing(self) -> None:
        ...

    def test_dups_fancy_indexing2(self) -> None:
        ...

    def test_duplicate_int_indexing(self, case: Any) -> None:
        ...

    def test_indexing_mixed_frame_bug(self):
        ...

    def test_multitype_list_index_access(self) -> None:
        ...

    def test_set_index_nan(self) -> None:
        ...

    def test_multi_assign(self) -> None:
        ...

    value: Any = ...
    def test_setitem_list(self):
        ...

    def test_string_slice(self) -> None:
        ...

    def test_astype_assignment(self) -> None:
        ...

    def test_index_contains(self, index: Any, val: Any) -> None:
        ...

    def test_index_not_contains(self, index: Any, val: Any) -> None:
        ...

    def test_mixed_index_contains(self, index: Any, val: Any) -> None:
        ...

    def test_mixed_index_not_contains(self, index: Any, val: Any) -> None:
        ...

    def test_contains_with_float_index(self) -> None:
        ...

    def test_index_type_coercion(self):
        ...


class TestMisc(Base):
    def test_float_index_to_mixed(self) -> None:
        ...

    def test_float_index_non_scalar_assignment(self) -> None:
        ...

    def test_float_index_at_iat(self) -> None:
        ...

    def test_mixed_index_assignment(self) -> None:
        ...

    def test_mixed_index_no_fallback(self) -> None:
        ...

    def test_rhs_alignment(self) -> None:
        ...

    def test_str_label_slicing_with_negative_step(self) -> None:
        ...

    def test_slice_with_zero_step_raises(self) -> None:
        ...

    def test_indexing_assignment_dict_already_exists(self) -> None:
        ...

    def test_indexing_dtypes_on_empty(self) -> None:
        ...

    def test_range_in_series_indexing(self) -> None:
        ...

    def test_non_reducing_slice(self) -> None:
        ...

    def test_list_slice(self) -> None:
        ...

    def test_maybe_numeric_slice(self) -> None:
        ...

    def test_partial_boolean_frame_indexing(self) -> None:
        ...

    def test_no_reference_cycle(self) -> None:
        ...


class TestSeriesNoneCoercion:
    EXPECTED_RESULTS: Any = ...
    def test_coercion_with_setitem(self) -> None:
        ...

    def test_coercion_with_loc_setitem(self) -> None:
        ...

    def test_coercion_with_setitem_and_series(self) -> None:
        ...

    def test_coercion_with_loc_and_series(self) -> None:
        ...


class TestDataframeNoneCoercion:
    EXPECTED_SINGLE_ROW_RESULTS: Any = ...
    def test_coercion_with_loc(self) -> None:
        ...

    def test_coercion_with_setitem_and_dataframe(self) -> None:
        ...

    def test_none_coercion_loc_and_dataframe(self) -> None:
        ...

    def test_none_coercion_mixed_dtypes(self) -> None:
        ...


def test_validate_indices_ok() -> None:
    ...

def test_validate_indices_low() -> None:
    ...

def test_validate_indices_high() -> None:
    ...

def test_validate_indices_empty() -> None:
    ...

def test_extension_array_cross_section() -> None:
    ...

def test_extension_array_cross_section_converts() -> None:
    ...

def test_ndframe_indexing_raises(idxr: Any, error: Any, error_message: Any) -> None:
    ...

def test_readonly_indices() -> None:
    ...
