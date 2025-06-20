from bot_types.base import Model


class ChatLink(Model):
    """
    Represents a chat link.

    Attributes:
        link (int | str): The unique identifier or URL of the chat link.
    """

    link: int | str
