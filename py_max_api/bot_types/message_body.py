from bot_types.base import Model
from bot_types.attachment import Attachment
from bot_types.markup_element import MarkupElement


class MessageBody(Model):
    """
    Represents the body of a message.

    Attributes:
        mid (str): The unique message identifier.
        seq (int): The sequence number of the message.
        text (str | None): The text content of the message, if any.
        attachments (list[Attachment] | None): List of attachments included in the message, if any.
        markup (list[MarkupElement] | None): List of markup elements (such as bold, italic, links) applied to the text, if any.
    """

    mid: str
    seq: int
    text: str | None = None
    attachments: list[Attachment] | None = None
    markup: list[MarkupElement] | None = None
