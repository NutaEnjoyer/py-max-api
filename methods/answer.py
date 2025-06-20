from methods.base import TelegramMethod
from typing import Any, Optional
from bot_types import (
    Message,
    AttachmentRequest,
    TextFormat,
    SuccessOrMessage,
    NewMessageBody,
)


class AnswerMethod(TelegramMethod):
    """
    Represents the 'answers' API method for sending a reply to a message.
    See: https://dev.max.ru/docs-api/methods/POST/answers
    """

    __returning__ = SuccessOrMessage
    __api_method__ = "answers"
    __api_method_type__ = "POST"

    def __init__(
        self,
        callback_id: str,
        message: NewMessageBody | None = None,
        notification: str | None = None,
    ):
        """
        :param callback_id: The ID of the callback to reply to.
        :param message: The message to reply to.
        :param notification: The notification to send.
        """
        super().__init__()

        self.params = {
            "callback_id": callback_id,
        }

        self.body = {
            "message": message.model_dump() if message else None,
            "notification": notification,
        }
