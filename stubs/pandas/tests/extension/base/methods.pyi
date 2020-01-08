# Stubs for pandas.tests.extension.base.methods (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,import-error

from typing import Any
from .base import BaseExtensionTests

class BaseMethodsTests(BaseExtensionTests):
    def test_value_counts(self, all_data: Any, dropna: Any) -> None:
        ...

    def test_count(self, data_missing: Any) -> None:
        ...

    def test_series_count(self, data_missing: Any) -> None:
        ...

    def test_apply_simple_series(self, data: Any) -> None:
        ...

    def test_argsort(self, data_for_sorting: Any) -> None:
        ...

    def test_argsort_missing_array(self, data_missing_for_sorting: Any) -> None:
        ...

    def test_argsort_missing(self, data_missing_for_sorting: Any) -> None:
        ...

    def test_nargsort(self, data_missing_for_sorting: Any, na_position: Any, expected: Any) -> None:
        ...

    def test_sort_values(self, data_for_sorting: Any, ascending: Any) -> None:
        ...

    def test_sort_values_missing(self, data_missing_for_sorting: Any, ascending: Any) -> None:
        ...

    def test_sort_values_frame(self, data_for_sorting: Any, ascending: Any) -> None:
        ...

    def test_unique(self, data: Any, box: Any, method: Any) -> None:
        ...

    def test_factorize(self, data_for_grouping: Any, na_sentinel: Any) -> None:
        ...

    def test_factorize_equivalence(self, data_for_grouping: Any, na_sentinel: Any) -> None:
        ...

    def test_factorize_empty(self, data: Any) -> None:
        ...

    def test_fillna_copy_frame(self, data_missing: Any) -> None:
        ...

    def test_fillna_copy_series(self, data_missing: Any) -> None:
        ...

    def test_fillna_length_mismatch(self, data_missing: Any) -> None:
        ...

    def test_combine_le(self, data_repeated: Any) -> None:
        ...

    def test_combine_add(self, data_repeated: Any) -> None:
        ...

    def test_combine_first(self, data: Any) -> None:
        ...

    def test_container_shift(self, data: Any, frame: Any, periods: Any, indices: Any) -> None:
        ...

    def test_shift_non_empty_array(self, data: Any, periods: Any, indices: Any) -> None:
        ...

    def test_shift_empty_array(self, data: Any, periods: Any) -> None:
        ...

    def test_shift_fill_value(self, data: Any) -> None:
        ...

    def test_hash_pandas_object_works(self, data: Any, as_frame: Any) -> None:
        ...

    def test_searchsorted(self, data_for_sorting: Any, as_series: Any) -> None:
        ...

    def test_where_series(self, data: Any, na_value: Any, as_frame: Any) -> None:
        ...

    def test_repeat(self, data: Any, repeats: Any, as_series: Any, use_numpy: Any) -> None:
        ...

    def test_repeat_raises(self, data: Any, repeats: Any, kwargs: Any, error: Any, msg: Any, use_numpy: Any) -> None:
        ...