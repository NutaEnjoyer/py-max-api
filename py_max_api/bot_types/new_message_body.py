from .base import Model
from .attachment_request import AttachmentRequest
from .new_message_link import NewMessageLink
from .text_format import TextFormat


class NewMessageBody(Model):
    """
    Represents the body of a new message to be sent.

    Attributes:
        text (str): The text content of the message.
        attachments (list[AttachmentRequest] | None): Optional list of attachments to include in the message.
        link (NewMessageLink | None): Optional link to another message (e.g., for replies or forwards).
        notify (bool | None): Whether to send a notification for this message. If None, the default behavior is used.
        format (TextFormat | None): Optional formatting for the message text (e.g., Markdown, HTML).
    """

    text: str
    attachments: list[AttachmentRequest] | None = None
    link: NewMessageLink | None = None
    notify: bool | None = None
    format: TextFormat | None = None
