# Stubs for pandas.tests.extension.test_numpy (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,too-many-ancestors

from typing import Any
from . import base

def dtype(request: Any) -> Any:
    ...

def allow_in_pandas(monkeypatch: Any) -> None:
    ...

def data(allow_in_pandas: Any, dtype: Any) -> Any:
    ...

def data_missing(allow_in_pandas: Any, dtype: Any) -> Any:
    ...

def na_value():
    ...

def na_cmp():
    ...

def data_for_sorting(allow_in_pandas: Any, dtype: Any) -> Any:
    ...

def data_missing_for_sorting(allow_in_pandas: Any, dtype: Any) -> Any:
    ...

def data_for_grouping(allow_in_pandas: Any, dtype: Any) -> Any:
    ...

def skip_numpy_object(dtype: Any) -> None:
    ...


skip_nested: Any

class BaseNumPyTests:
    ...


class TestCasting(BaseNumPyTests, base.BaseCastingTests):
    def test_astype_str(self, data: Any) -> None:
        ...


class TestConstructors(BaseNumPyTests, base.BaseConstructorsTests):
    def test_from_dtype(self, data: Any) -> None:
        ...

    def test_array_from_scalars(self, data: Any) -> None:
        ...


class TestDtype(BaseNumPyTests, base.BaseDtypeTests):
    def test_check_dtype(self, data: Any) -> None:
        ...


class TestGetitem(BaseNumPyTests, base.BaseGetitemTests):
    def test_getitem_scalar(self, data: Any) -> None:
        ...

    def test_take_series(self, data: Any) -> None:
        ...

    def test_loc_iloc_frame_single_dtype(self, data: Any) -> None:
        ...


class TestGroupby(BaseNumPyTests, base.BaseGroupbyTests):
    def test_groupby_extension_apply(self, data_for_grouping: Any, groupby_apply_op: Any) -> None:
        ...


class TestInterface(BaseNumPyTests, base.BaseInterfaceTests):
    def test_array_interface(self, data: Any) -> None:
        ...


class TestMethods(BaseNumPyTests, base.BaseMethodsTests):
    def test_value_counts(self, all_data: Any, dropna: Any) -> None:
        ...

    def test_combine_le(self, data_repeated: Any) -> None:
        ...

    def test_combine_add(self, data_repeated: Any) -> None:
        ...

    def test_shift_fill_value(self, data: Any) -> None:
        ...

    def test_unique(self, data: Any, box: Any, method: Any) -> None:
        ...

    def test_fillna_copy_frame(self, data_missing: Any) -> None:
        ...

    def test_fillna_copy_series(self, data_missing: Any) -> None:
        ...

    def test_hash_pandas_object_works(self, data: Any, as_frame: Any) -> None:
        ...

    def test_searchsorted(self, data_for_sorting: Any, as_series: Any) -> None:
        ...

    def test_where_series(self, data: Any, na_value: Any, as_frame: Any) -> None:
        ...

    def test_repeat(self, data: Any, repeats: Any, as_series: Any, use_numpy: Any) -> None:
        ...


class TestArithmetics(BaseNumPyTests, base.BaseArithmeticOpsTests):
    divmod_exc: Any = ...
    series_scalar_exc: Any = ...
    frame_scalar_exc: Any = ...
    series_array_exc: Any = ...
    def test_divmod_series_array(self, data: Any) -> None:  # type: ignore
        ...

    def test_error(self, data: Any, all_arithmetic_operators: Any) -> None:
        ...

    def test_arith_series_with_scalar(self, data: Any, all_arithmetic_operators: Any) -> None:
        ...

    def test_arith_series_with_array(self, data: Any, all_arithmetic_operators: Any) -> None:
        ...


class TestPrinting(BaseNumPyTests, base.BasePrintingTests):
    ...


class TestNumericReduce(BaseNumPyTests, base.BaseNumericReduceTests):
    def check_reduce(self, s: Any, op_name: Any, skipna: Any) -> None:
        ...


class TestBooleanReduce(BaseNumPyTests, base.BaseBooleanReduceTests):
    ...


class TestMissing(BaseNumPyTests, base.BaseMissingTests):
    def test_fillna_scalar(self, data_missing: Any) -> None:
        ...

    def test_fillna_series_method(self, data_missing: Any, fillna_method: Any) -> None:
        ...

    def test_fillna_series(self, data_missing: Any) -> None:
        ...

    def test_fillna_frame(self, data_missing: Any) -> None:
        ...


class TestReshaping(BaseNumPyTests, base.BaseReshapingTests):
    def test_concat_mixed_dtypes(self, data: Any) -> None:
        ...

    def test_merge(self, data: Any, na_value: Any) -> None:
        ...

    def test_merge_on_extension_array(self, data: Any) -> None:
        ...

    def test_merge_on_extension_array_duplicates(self, data: Any) -> None:
        ...


class TestSetitem(BaseNumPyTests, base.BaseSetitemTests):
    def test_setitem_scalar_series(self, data: Any, box_in_series: Any) -> None:
        ...

    def test_setitem_sequence(self, data: Any, box_in_series: Any) -> None:
        ...

    def test_setitem_sequence_mismatched_length_raises(self, data: Any, as_array: Any) -> None:
        ...

    def test_setitem_sequence_broadcasts(self, data: Any, box_in_series: Any) -> None:
        ...

    def test_setitem_loc_scalar_mixed(self, data: Any) -> None:
        ...

    def test_setitem_loc_scalar_multiple_homogoneous(self, data: Any) -> None:
        ...

    def test_setitem_iloc_scalar_mixed(self, data: Any) -> None:
        ...

    def test_setitem_iloc_scalar_multiple_homogoneous(self, data: Any) -> None:
        ...

    def test_setitem_mask_broadcast(self, data: Any, setter: Any) -> None:
        ...

    def test_setitem_scalar_key_sequence_raise(self, data: Any) -> None:
        ...


class TestParsing(BaseNumPyTests, base.BaseParsingTests):
    ...