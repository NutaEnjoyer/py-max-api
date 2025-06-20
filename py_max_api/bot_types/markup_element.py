from pydantic import Field
from bot_types.base import Model
from bot_types.markup_element_type import MarkupElementType


class MarkupElement(Model):
    """
    Represents a markup element within a text, such as bold, italic, or a link.

    Attributes:
        type_ (MarkupElementType): The type of markup element (e.g., bold, italic, link), aliased as "type".
        from_ (int): The starting position of the markup element in the text, aliased as "from".
        length (int): The length of the markup element in characters.
    """

    type_: MarkupElementType = Field(alias="type")
    from_: int = Field(alias="from")
    length: int
