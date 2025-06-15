from pydantic import Field
from bot_types.base import Model
from bot_types.markup_element_type import MarkupElementType


class MarkupElement(Model):
    type_: MarkupElementType = Field(alias="type")
    from_: int = Field(alias="from")
    length: int
