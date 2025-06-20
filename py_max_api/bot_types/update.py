from .message import Message
from .update_type import UpdateType
from .base import Model


class Update(Model):
    """
    Represents an update event in the bot system.

    Attributes:
        update_type (UpdateType): The type of the update event.
        timestamp (int): The Unix timestamp when the update occurred.
        message (Message): The message associated with the update.
        user_locale (str | None): The locale of the user, if available.
    """

    update_type: UpdateType
    timestamp: int
    message: Message
    user_locale: str | None = None
