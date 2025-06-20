from enum import Enum


class MessageLinkType(str, Enum):
    """
    Enum representing different types of message links.

    Attributes:
        FORWARD: Represents a forwarded message.
        REPLY: Represents a replied message.
    """

    FORWARD = "forward"
    REPLY = "reply"
