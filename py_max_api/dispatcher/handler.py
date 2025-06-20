"""
This module defines the Handler class used by the Dispatcher to store handler functions
and their associated update types, commands, and filters for the MAX API bot.
"""

from typing import Callable
from bot_types import UpdateType
from filters import Filter


class Handler:
    """
    Represents a handler for a specific update type in the Dispatcher.
    Stores the handler function, update type, commands, and filters.
    """

    def __init__(
        self,
        func: Callable,
        update_type: UpdateType,
        commands: list[str] | None = None,
        filters: list[Filter] | None = None,
    ):
        """
        Initialize a Handler instance.
        :param func: The handler function to be called for the update.
        :param update_type: The type of update this handler responds to.
        :param commands: List of commands that trigger this handler (optional).
        :param filters: List of filters to apply to the update (optional).
        """
        self.func = func
        self.update_type = update_type
        self.commands = (
            [f"/{command.lower()}" for command in commands] if commands else None
        )
        self.filters = filters
