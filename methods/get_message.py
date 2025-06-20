from methods.base import TelegramMethod
from bot_types.message import Message


class GetMessageMethod(TelegramMethod):
    __returning__ = Message
    __api_method__ = "messages"
    __api_method_type__ = "GET"

    def __init__(
        self,
        message_id: str,
    ):
        super().__init__()
        self.uri = message_id
