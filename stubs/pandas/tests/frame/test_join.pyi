# Stubs for pandas.tests.frame.test_join (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level

from typing import Any


def frame_with_period_index() -> Any:
    ...


def left() -> Any:
    ...


def right() -> Any:
    ...


def test_join(
        left: Any, right: Any, how: Any, sort: Any, expected: Any) -> None:
    ...


def test_join_index(float_frame: Any) -> None:
    ...


def test_join_index_more(float_frame: Any) -> None:
    ...


def test_join_index_series(float_frame: Any) -> None:
    ...


def test_join_overlap(float_frame: Any) -> None:
    ...


def test_join_period_index(frame_with_period_index: Any) -> None:
    ...


def test_join_left_sequence_non_unique_index() -> None:
    ...