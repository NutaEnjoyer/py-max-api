import requests

from bot_types import Me
from methods import (
    GetMeMethod,
    GetChatsMethod,
    SendMessageMethod,
    UpdateMeMethod,
    GetMessagesMethod,
    UploadMethod,
    GetChatMethod,
)

from client.session import Session

from bot_types.upload_type import UploadType


class Bot:
    BASE_URL = "https://botapi.max.ru{methodName}"

    def __init__(
        self,
        token: str,
        request_timeout: int = 50,
        **kwargs: any,
    ) -> None:

        self.__token = token
        self.request_timeout = request_timeout
        self.session = Session(self)
        self.params = {"access_token": self.__token}

    def __call__(self, method):
        response = self.session(method, timeout=self.request_timeout)
        return response

    @property
    def token(self):
        return self.__token

    def get_me(self) -> GetMeMethod.returning:
        call = GetMeMethod()

        return self(call)

    def update_me(self, *args, **kwargs) -> UpdateMeMethod.returning:
        call = UpdateMeMethod(*args, **kwargs)

        return self(call)

    def get_chat(self, *args, **kwargs) -> GetChatMethod.returning:
        call = GetChatMethod(*args, **kwargs)
        return self(call)

    def get_chats(self) -> GetChatsMethod.returning:
        call = GetChatsMethod()

        return self(call)

    def send_message(self, *args, **kwargs) -> SendMessageMethod.returning:
        """
        Send message

        - `user_id`
        - `chat_id`
        - `text`
        """
        call = SendMessageMethod(*args, **kwargs)

        return self(call)

    def get_messages(self, *args, **kwargs) -> GetMessagesMethod.returning:
        call = GetMessagesMethod(*args, **kwargs)

        return self(call)

    def upload_photo(
        self,
        path: str,
    ) -> UploadMethod.returning:
        call = UploadMethod(path=path, type_=UploadType.IMAGE)
        return self(call)
