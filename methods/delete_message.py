from .base import TelegramMethod
from bot_types import SuccessOrMessage


class DeleteMessageMethod(TelegramMethod):
    __returning__ = SuccessOrMessage
    __api_method__ = "messages"
    __api_method_type__ = "DELETE"
    __return_key__ = None

    def __init__(self, message_id: str):
        super().__init__()
        self.params = {"message_id": message_id}
