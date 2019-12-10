# Stubs for pandas.tests.io.formats.test_to_html (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member,too-many-ancestors

from typing import Any

lorem_ipsum: str

def expected_html(datapath: Any, name: Any) -> Any:
    ...


def biggie_df_fixture(request: Any) -> Any:
    ...


def justify(request: Any) -> Any:
    ...


def test_to_html_with_col_space(col_space: Any) -> None:
    ...


def test_to_html_with_empty_string_label() -> None:
    ...


def test_to_html_unicode(df: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_decimal(datapath: Any) -> None:
    ...


def test_to_html_escaped(kwargs: Any, string: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_multiindex_index_false(index_is_named: Any, datapath: Any) -> None:
    ...


def test_to_html_multiindex_sparsify(multi_sparse: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_multiindex_odd_even_truncate(max_rows: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_formatters(df: Any, formatters: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_regression_GH6098() -> None:
    ...


def test_to_html_truncate(datapath: Any) -> None:
    ...


def test_to_html_truncate_multi_index(sparsify: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_border(option: Any, result: Any, expected: Any) -> None:
    ...


def test_to_html(biggie_df_fixture: Any) -> None:
    ...


def test_to_html_empty_dataframe(biggie_df_fixture: Any) -> None:
    ...


def test_to_html_filename(biggie_df_fixture: Any, tmpdir: Any) -> None:
    ...


def test_to_html_with_no_bold() -> None:
    ...


def test_to_html_columns_arg(float_frame: Any) -> None:
    ...


def test_to_html_multiindex(columns: Any, justify: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_justify(justify: Any, datapath: Any) -> None:
    ...


def test_to_html_invalid_justify(justify: Any) -> None:
    ...


def test_to_html_index(datapath: Any) -> None:
    ...


def test_to_html_with_classes(classes: Any, datapath: Any) -> None:
    ...


def test_to_html_no_index_max_rows(datapath: Any) -> None:
    ...


def test_to_html_multiindex_max_cols(datapath: Any) -> None:
    ...


def test_to_html_multi_indexes_index_false(datapath: Any) -> None:
    ...


def test_to_html_basic_alignment(datapath: Any, row_index: Any, row_type: Any, column_index: Any, column_type: Any, index: Any, header: Any, index_names: Any) -> None:
    ...


def test_to_html_alignment_with_truncation(datapath: Any, row_index: Any, row_type: Any, column_index: Any, column_type: Any, index: Any, header: Any, index_names: Any) -> None:
    ...


def test_to_html_truncation_index_false_max_rows(datapath: Any, index: Any) -> None:
    ...


def test_to_html_truncation_index_false_max_cols(datapath: Any, index: Any, col_index_named: Any, expected_output: Any) -> None:
    ...


def test_to_html_notebook_has_style(notebook: Any) -> None:
    ...


def test_to_html_with_index_names_false() -> None:
    ...


def test_to_html_with_id() -> None:
    ...


def test_to_html_float_format_no_fixed_width(value: Any, float_format: Any, expected: Any, datapath: Any) -> None:
    ...


def test_to_html_render_links(render_links: Any, expected: Any, datapath: Any) -> None:
    ...


def test_ignore_display_max_colwidth(method: Any, expected: Any, max_colwidth: Any) -> None:
    ...


def test_to_html_invalid_classes_type(classes: Any) -> None:
    ...


def test_to_html_round_column_headers() -> None:
    ...


def test_to_html_with_col_space_units(unit: Any) -> None:
    ...
