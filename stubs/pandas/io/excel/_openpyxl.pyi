# Stubs for pandas.io.excel._openpyxl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any, List, Optional
from pandas._typing import FilePathOrBuffer, Scalar
from pandas.io.excel._base import ExcelWriter, _BaseExcelReader

class _OpenpyxlWriter(ExcelWriter):
    engine: str = ...
    supported_extensions: Any = ...
    book: Any = ...
    def __init__(self, path: Any, engine: Optional[Any] = ..., mode: str = ..., **engine_kwargs: Any) -> None:
        ...

    def save(self):
        ...

    def write_cells(self, cells: Any, sheet_name: Optional[Any] = ..., startrow: int = ..., startcol: int = ..., freeze_panes: Optional[Any] = ...) -> None:
        ...


class _OpenpyxlReader(_BaseExcelReader):
    def __init__(self, filepath_or_buffer: FilePathOrBuffer) -> None:
        ...

    def load_workbook(self, filepath_or_buffer: FilePathOrBuffer) -> Any:
        ...

    @property
    def sheet_names(self) -> List[str]:
        ...

    def get_sheet_by_name(self, name: str) -> Any:
        ...

    def get_sheet_by_index(self, index: int) -> Any:
        ...

    def get_sheet_data(self, sheet: Any, convert_float: bool) -> List[List[Scalar]]:
        ...
