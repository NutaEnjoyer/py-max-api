from methods.base import TelegramMethod
from bot_types import Me
from bot_types.bot_command import BotCommand
from bot_types.photo_attachment_request_payload import PhotoAttachmentRequestPayload


class UpdateMeMethod(TelegramMethod):
    __returning__ = Me
    __api_method__ = "me"
    __api_method_type__ = "PATCH"

    def __init__(
        self,
        name: str | None = None,
        description: str | None = None,
        commands: list[BotCommand] | None = None,
        photo: PhotoAttachmentRequestPayload | None = None,
    ):
        super().__init__()
        self.body = {
            "name": name,
            "description": description,
            "commands": [cmd.model_dump() for cmd in commands] if commands else None,
            "photo": photo.model_dump() if photo else None,
        }
