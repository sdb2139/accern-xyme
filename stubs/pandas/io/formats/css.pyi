# Stubs for pandas.io.formats.css (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-argument,redefined-outer-name,no-self-use,invalid-name
# pylint: disable=relative-beyond-top-level,line-too-long,arguments-differ
# pylint: disable=no-member,too-few-public-methods,keyword-arg-before-vararg
# pylint: disable=super-init-not-called,abstract-method,redefined-builtin
# pylint: disable=unused-import,useless-import-alias,signature-differs
# pylint: disable=blacklisted-name,c-extension-no-member

from typing import Any, Optional

class CSSWarning(UserWarning):
    ...


class CSSResolver:
    def __call__(self, declarations_str: Any, inherited: Optional[Any] = ...) -> Any:
        ...

    UNIT_RATIOS: Any = ...
    FONT_SIZE_RATIOS: Any = ...
    MARGIN_RATIOS: Any = ...
    BORDER_WIDTH_RATIOS: Any = ...
    def size_to_pt(self, in_val: Any, em_pt: Optional[Any] = ..., conversions: Any = ...) -> Any:
        ...

    def atomize(self, declarations: Any) -> None:
        ...

    SIDE_SHORTHANDS: Any = ...
    SIDES: Any = ...
    expand_border_color: Any = ...
    expand_border_style: Any = ...
    expand_border_width: Any = ...
    expand_margin: Any = ...
    expand_padding: Any = ...
    def parse(self, declarations_str: Any) -> None:
        ...
