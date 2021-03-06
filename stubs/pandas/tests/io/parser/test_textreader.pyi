# Stubs for pandas.tests.io.parser.test_textreader (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin

from typing import Any

class TestTextReader:
    dirpath: Any = ...
    csv1: Any = ...
    csv2: Any = ...
    xls1: Any = ...
    def setup_method(self, datapath: Any) -> None:
        ...

    def test_file_handle(self) -> None:
        ...

    def test_string_filename(self) -> None:
        ...

    def test_file_handle_mmap(self) -> None:
        ...

    def test_StringIO(self) -> None:
        ...

    def test_string_factorize(self) -> None:
        ...

    def test_skipinitialspace(self) -> None:
        ...

    def test_parse_booleans(self) -> None:
        ...

    def test_delimit_whitespace(self) -> None:
        ...

    def test_embedded_newline(self) -> None:
        ...

    def test_euro_decimal(self) -> None:
        ...

    def test_integer_thousands(self) -> None:
        ...

    def test_integer_thousands_alt(self) -> None:
        ...

    def test_skip_bad_lines(self, capsys: Any) -> None:
        ...

    def test_header_not_enough_lines(self) -> None:
        ...

    def test_escapechar(self) -> None:
        ...

    def test_eof_has_eol(self) -> None:
        ...

    def test_na_substitution(self) -> None:
        ...

    def test_numpy_string_dtype(self) -> None:
        ...

    def test_pass_dtype(self) -> None:
        ...

    def test_usecols(self) -> None:
        ...

    def test_cr_delimited(self) -> None:
        ...

    def test_empty_field_eof(self) -> None:
        ...

    def test_empty_csv_input(self) -> None:
        ...


def assert_array_dicts_equal(left: Any, right: Any) -> None:
    ...
