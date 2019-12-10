# pylint: disable=unused-import,unused-argument
# pylint: disable=too-few-public-methods,no-self-use

from typing import Any
# TODO: add better annotations when ctypes is stubbed out


class _ctypes:
    @property
    def data(self) -> int:
        ...

    @property
    def shape(self) -> Any:
        ...

    @property
    def strides(self) -> Any:
        ...

    def data_as(self, obj: Any) -> Any:
        ...

    def shape_as(self, obj: Any) -> Any:
        ...

    def strides_as(self, obj: Any) -> Any:
        ...

    def get_data(self) -> int:
        ...

    def get_shape(self) -> Any:
        ...

    def get_strides(self) -> Any:
        ...

    def get_as_parameter(self) -> Any:
        ...
