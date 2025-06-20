from bot_types import Me
from methods.base import TelegramMethod
from bot_types.message import Message


class GetMessagesMethod(TelegramMethod):

    __returning__ = list[Message]
    __api_method__ = "messages"
    __api_method_type__ = "GET"
    __return_key__ = "messages"

    def __init__(
        self,
        chat_id: int | None = None,
        message_ids: list[str] | None = None,
        from_: int | None = None,
        to: int | None = None,
        count: int | None = None,
    ):
        super().__init__()
        self.params = {
            "chat_id": chat_id,
            "message_ids": (
                ",".join([m for m in message_ids]) if message_ids else None
            ),
            "from": from_,
            "to": to,
            "count": count,
        }
