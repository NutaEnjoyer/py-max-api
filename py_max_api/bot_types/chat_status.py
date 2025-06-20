from enum import Enum


class ChatStatus(str, Enum):
    """
    Enum representing the possible statuses of a chat.

    Attributes:
        ACTIVE: The chat is currently active.
        REMOVED: The chat has been removed.
        LEFT: The user has left the chat.
        CLOSED: The chat has been closed.
        SUSPENDED: The chat has been suspended.
    """

    ACTIVE = "active"
    REMOVED = "removed"
    LEFT = "left"
    CLOSED = "closed"
    SUSPENDED = "suspended"
