from methods.base import TelegramMethod
from bot_types.chat import Chat
from bot_types.chat_link import ChatLink


class GetChatMethod(TelegramMethod):

    def __init__(self, chat_link: int | str):
        super().__init__()
        self.uri = chat_link

    __api_method__ = "chats"
    __returning__ = Chat
    __api_method_type__ = "GET"
    # __return_key__ = "chats"
