from enum import Enum


class MarkupElementType(str, Enum):
    """
    Enum representing different types of markup elements that can be used in text formatting.

    Attributes:
        STRONG: Represents bold or strong emphasis.
        EMPHASIZED: Represents emphasized or italicized text.
        MONOSPACED: Represents monospaced or code-formatted text.
        LINK: Represents a hyperlink.
        STRIKETHROUGH: Represents text with a strikethrough.
        UNDERLINED: Represents underlined text.
        USER_MENTION: Represents a mention of a user.
        HEADING: Represents a heading or title.
        HIGHLIGHTED: Represents highlighted text.
    """

    STRONG = "strong"
    EMPHASIZED = "emphasized"
    MONOSPACED = "monospaced"
    LINK = "link"
    STRIKETHROUGH = "strikethrough"
    UNDERLINED = "underlined"
    USER_MENTION = "user_mention"
    HEADING = "heading"
    HIGHLIGHTED = "highlighted"
