from .base import Model
from .update import Update


class Updates(Model):
    """
    Represents a collection of update events received by the bot.

    Attributes:
        updates (list[Update]): A list of update events.
        marker (int | None): An optional marker for pagination or tracking the last received update.
    """

    updates: list[Update]
    marker: int | None = None
