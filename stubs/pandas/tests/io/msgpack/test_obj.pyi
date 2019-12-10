# Stubs for pandas.tests.io.msgpack.test_obj (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

class DecodeError(Exception):
    ...


class TestObj:
    def bad_complex_decoder(self, o: Any) -> None:
        ...

    def test_encode_hook(self) -> None:
        ...

    def test_decode_hook(self) -> None:
        ...

    def test_decode_pairs_hook(self) -> None:
        ...

    def test_only_one_obj_hook(self) -> None:
        ...

    def test_bad_hook(self) -> None:
        ...

    def test_array_hook(self) -> None:
        ...

    def test_an_exception_in_objecthook1(self) -> None:
        ...

    def test_an_exception_in_objecthook2(self) -> None:
        ...
