from bot_types import Me
from methods.base import TelegramMethod
from bot_types.attachment_request import AttachmentRequest
from bot_types.new_message_link import NewMessageLink
from bot_types.text_format import TextFormat
from bot_types.message import Message


class SendMessageMethod(TelegramMethod):

    __returning__ = Message
    __api_method__ = "messages"
    __api_method_type__ = "POST"
    __return_key__ = "message"

    def __init__(
        self,
        user_id: int | None = None,
        chat_id: int | None = None,
        text: str | None = None,
        attachments: list[AttachmentRequest] | None = None,
        link: NewMessageLink | None = None,
        norify: bool = True,
        format: TextFormat | None = None,
        disable_link_preview: bool | None = None,
    ):
        super().__init__()
        self.params = {
            "user_id": user_id,
            "chat_id": chat_id,
            "disable_link_preview": disable_link_preview,
        }

        self.body = {
            "text": text,
            "attachments": (
                [at.model_dump() for at in attachments] if attachments else None
            ),
            "link": link.model_dump() if link else None,
            "notify": norify,
            "format": format.value if format else None,
        }
