from bot_types.base import Model
from bot_types.attachment import Attachment
from bot_types.markup_element import MarkupElement


class MessageBody(Model):
    mid: str
    seq: int
    text: str | None = None
    attachments: list[Attachment] | None = None
    markup: list[MarkupElement] | None = None
