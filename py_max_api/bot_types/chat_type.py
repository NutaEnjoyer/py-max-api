from enum import Enum


class ChatType(str, Enum):
    """
    Enum representing the different types of chats.

    Attributes:
        DIALOG: Represents a one-on-one chat.
        CHAT: Represents a group chat.
    """

    DIALOG = "dialog"
    CHAT = "chat"
