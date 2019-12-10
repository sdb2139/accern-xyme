# Stubs for pandas.tests.util.test_hashing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any


def series(request: Any) -> Any:
    ...


def index(request: Any) -> Any:
    ...


def test_consistency() -> None:
    ...


def test_hash_array(series: Any) -> None:
    ...


def test_hash_array_mixed(arr2: Any) -> None:
    ...


def test_hash_array_errors(val: Any) -> None:
    ...


def test_hash_tuples() -> None:
    ...


def test_hash_tuple(tup: Any) -> None:
    ...


def test_hash_scalar(val: Any) -> None:
    ...


def test_hash_tuples_err(val: Any) -> None:
    ...


def test_multiindex_unique() -> None:
    ...


def test_multiindex_objects() -> None:
    ...


def test_hash_pandas_object(obj: Any, index: Any) -> None:
    ...


def test_hash_pandas_object2(series: Any, index: Any) -> None:
    ...


def test_hash_pandas_empty_object(obj: Any, index: Any) -> None:
    ...


def test_categorical_consistency(s1: Any, categorize: Any) -> None:
    ...


def test_categorical_with_nan_consistency() -> None:
    ...


def test_pandas_errors(obj: Any) -> None:
    ...


def test_hash_keys() -> None:
    ...


def test_invalid_key() -> None:
    ...


def test_already_encoded(index: Any) -> None:
    ...


def test_alternate_encoding(index: Any) -> None:
    ...


def test_same_len_hash_collisions(l_exp: Any, l_add: Any) -> None:
    ...


def test_hash_collisions() -> None:
    ...
