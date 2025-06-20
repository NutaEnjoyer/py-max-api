from .base import Model
from .attachment_request import AttachmentRequest
from .new_message_link import NewMessageLink
from .text_format import TextFormat


class NewMessageBody(Model):
    text: str
    attachments: list[AttachmentRequest] | None = None
    link: NewMessageLink | None = None
    notify: bool | None = None
    format: TextFormat | None = None
