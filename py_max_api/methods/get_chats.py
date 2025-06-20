from methods.base import TelegramMethod
from bot_types.chat import Chat


class GetChatsMethod(TelegramMethod):

    def __init__(self, count: int | None = None, marker: int | None = None):
        super().__init__()
        self.params = {"count": count, "marker": marker}

    __returning__ = list[Chat]
    __api_method__ = "chats"
    __api_method_type__ = "GET"
    __return_key__ = "chats"
