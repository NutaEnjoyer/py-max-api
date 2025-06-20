from enum import Enum


class TextFormat(Enum):
    """
    Enum representing the available text formatting options.

    Attributes:
        MARKDOWN: Markdown formatting.
        HTML: HTML formatting.
    """

    MARKDOWN = "markdown"
    HTML = "html"
