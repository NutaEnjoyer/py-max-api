from bot_types.new_message_link import NewMessageLink
from bot_types.success_or_message import SuccessOrMessage
from methods.base import TelegramMethod
from bot_types.message import Message
from bot_types.text_format import TextFormat
from bot_types.attachment_request import AttachmentRequest


class EditMessageMethod(TelegramMethod):
    __returning__ = SuccessOrMessage
    __api_method__ = "messages"
    __api_method_type__ = "PUT"

    def __init__(
        self,
        message_id: str,
        text: str | None = None,
        attachments: list[AttachmentRequest] | None = None,
        link: NewMessageLink | None = None,
        notify: bool | None = None,
        format: TextFormat | None = None,
    ):
        super().__init__()
        self.params = {"message_id": message_id}
        self.body = {
            "text": text,
            "attachments": (
                [at.model_dump() for at in attachments] if attachments else None
            ),
            "link": link.model_dump() if link else None,
            "notify": notify,
            "format": format.value if format else None,
        }
