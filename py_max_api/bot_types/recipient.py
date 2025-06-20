from bot_types.base import Model
from bot_types.chat_type import ChatType


class Recipient(Model):
    """
    Represents a recipient of a message.

    Attributes:
        chat_id (int): The unique identifier of the chat.
        chat_type (ChatType): The type of the chat (e.g., private, group).
        user_id (int | None): The unique identifier of the user, if applicable.
    """

    chat_id: int
    chat_type: ChatType
    user_id: int | None = None
