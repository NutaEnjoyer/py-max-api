from typing import Any

from bot_types import (
    Me,
    Chat,
    Message,
    Upload,
    AttachmentRequest,
    NewMessageLink,
    SuccessOrMessage,
    TextFormat,
    UploadType,
    NewMessageBody,
    Video,
)

from methods import (
    GetMeMethod,
    GetChatsMethod,
    SendMessageMethod,
    UpdateMeMethod,
    GetMessagesMethod,
    UploadMethod,
    GetChatMethod,
    DeleteMessageMethod,
    EditMessageMethod,
    GetMessageMethod,
    AnswerMethod,
    GetVideoMethod,
)

from client.session import Session


class Bot:
    """
    Main interface for interacting with the MAX API as a bot.
    Provides methods for user, chat, message, and file operations.
    """

    BASE_URL = "https://botapi.max.ru{methodName}"

    def __init__(
        self,
        token: str,
        request_timeout: int = 15,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the Bot instance.
        :param token: Bot access token.
        :param request_timeout: Default timeout for API requests (seconds).
        :param kwargs: Additional parameters (unused).
        """
        self.__token = token
        self.request_timeout = request_timeout
        self.session = Session(self)
        self.params = {"access_token": self.__token}
        self.verify = False

    def __call__(self, method) -> Any:
        """
        Execute an API method using the session with the default timeout.
        :param method: The API method instance to execute.
        :return: The parsed API response.
        """
        response = self.session(method, timeout=self.request_timeout)
        return response

    @property
    def token(self):
        """
        Get the bot's access token.
        :return: The access token string.
        """
        return self.__token

    def get_me(self) -> Me:
        """
        Get information about the current bot.
        :return: Me model with bot info.
        """
        call = GetMeMethod()
        return self(call)

    def update_me(self, *args, **kwargs) -> Me:
        """
        Update the bot's profile information.
        :param args: Positional arguments for UpdateMeMethod.
        :param kwargs: Keyword arguments for UpdateMeMethod.
        :return: Updated Me model.
        """
        call = UpdateMeMethod(*args, **kwargs)
        return self(call)

    def get_chat(self, *args, **kwargs) -> Chat:
        """
        Get information about a specific chat.
        :param args: Positional arguments for GetChatMethod.
        :param kwargs: Keyword arguments for GetChatMethod.
        :return: Chat model.
        """
        call = GetChatMethod(*args, **kwargs)
        return self(call)

    def get_chats(self) -> list[Chat]:
        """
        Get a list of all chats the bot is a member of.
        :return: List of Chat models.
        """
        call = GetChatsMethod()
        return self(call)

    def send_message(
        self,
        user_id: int | None = None,
        chat_id: int | None = None,
        text: str | None = None,
        attachments: list[AttachmentRequest] | None = None,
        link: NewMessageLink | None = None,
        notify: bool | None = None,
        format: TextFormat | None = None,
        disable_link_preview: bool | None = None,
    ) -> Message:
        """
        Send a message to a user or chat.
        :param user_id: User ID.
        :param chat_id: Chat ID.
        :param text: Message text.
        :param attachments: List of attachments.
        :param link: Link to the message.
        :param notify: Notify the user.
        :param format: Format of the message.
        :param disable_link_preview: Disable link preview.
        :return: Sent Message model.
        """
        call = SendMessageMethod(
            user_id=user_id,
            chat_id=chat_id,
            text=text,
            attachments=attachments,
            link=link,
            notify=notify,
            format=format,
            disable_link_preview=disable_link_preview,
        )
        return self(call)

    def get_message(self, message_id: str) -> Message:
        """
        Get a message by its ID.
        :param message_id: Message ID.
        :return: Message model.
        """
        call = GetMessageMethod(message_id=message_id)
        return self(call)

    def get_messages(
        self,
        chat_id: int | None = None,
        message_ids: list[str] | None = None,
        from_: int | None = None,
        to: int | None = None,
        count: int | None = None,
    ) -> list[Message]:
        """
        Get messages from a chat.
        :param chat_id: Chat ID.
        :param message_ids: List of message IDs.
        :param from_: From message ID.
        :param to: To message ID.
        :param count: Count of messages to get.
        :return: List of Message models.
        """
        call = GetMessagesMethod(
            chat_id=chat_id,
            message_ids=message_ids,
            from_=from_,
            to=to,
            count=count,
        )
        return self(call)

    def edit_message(self, *args, **kwargs) -> SuccessOrMessage:
        """
        Edit a message.
        :param args: Positional arguments for EditMessageMethod.
        :param kwargs: Keyword arguments for EditMessageMethod.
        :return: SuccessOrMessage model.
        """
        call = EditMessageMethod(*args, **kwargs)
        return self(call)

    def delete_message(self, message_id: str) -> SuccessOrMessage:
        """
        Delete a message.
        :param message_id: Message ID.
        :return: SuccessOrMessage model.
        """
        call = DeleteMessageMethod(message_id=message_id)
        return self(call)

    def upload_photo(
        self,
        path: str,
    ) -> Upload:
        """
        Upload a photo file to the server.
        :param path: Path to the photo file.
        :return: Upload model with file URL.
        """
        call = UploadMethod(path=path, type_=UploadType.IMAGE)
        return self(call)

    def upload_video(
        self,
        path: str,
    ) -> Upload:
        """
        Upload a video file to the server.
        :param path: Path to the video file.
        :return: Upload model with file URL.
        """
        call = UploadMethod(path=path, type_=UploadType.VIDEO)
        return self(call)

    def get_video(self, video_token: str) -> Video:
        """
        Get a video by its token.
        :param video_token: Video token.
        :return: Video model.
        """
        call = GetVideoMethod(video_token=video_token)
        return self(call)

    def answer(
        self,
        callback_id: str,
        message: NewMessageBody | None = None,
        notification: str | None = None,
    ) -> SuccessOrMessage:
        """
        Answer a callback.
        :param callback_id: The ID of the callback to answer.
        :param message: The message to answer.
        :param notification: The notification to send.
        """

        call = AnswerMethod(
            callback_id=callback_id,
            message=message,
            notification=notification,
        )
        return self(call)
