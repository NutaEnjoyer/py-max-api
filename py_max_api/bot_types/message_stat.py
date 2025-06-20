from bot_types.base import Model


class MessageStat(Model):
    """
    Represents statistics for a message.

    Attributes:
        views (int): The number of times the message has been viewed.
    """

    views: int
