"""
This module provides the Dispatcher class for handling updates from the MAX API.
It allows registration of handler functions for different update types using decorators
and dispatches incoming updates to the appropriate handlers.
"""

from configs import config
from .handler import Handler
from filters import Filter
from bot_types import Update, UpdateType
from typing import Callable
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class Dispatcher:
    """
    Event dispatcher for handling updates from the MAX API.
    Allows registration of handler functions for different update types using decorators.
    """

    def __init__(self, bot):
        """
        Initialize the Dispatcher with a bot instance.
        :param bot: The bot instance to dispatch updates for.
        """
        self.bot = bot
        self.handlers = []

    def add_handler(self, handler: Handler):
        """
        Add a handler to the dispatcher.
        :param handler: Handler instance to add.
        """
        self.handlers.append(handler)

    async def handle(self, update: Update):
        """
        Dispatch an incoming update to the appropriate handler.
        :param update: The update to handle.
        :return: The result of the handler function, if any.
        """
        for handler in self.handlers:
            if handler.update_type == update.update_type:
                if handler.filters:
                    if not all(filter.check(update) for filter in handler.filters):
                        continue

                if handler.commands:
                    if update.message.text in handler.commands:
                        return await handler.func(update)
                    else:
                        continue

                else:
                    return await handler.func(update)

    def message_handler(
        self, commands: list[str] | None = None, filters: list[Filter] | None = None
    ):
        """
        Decorator to register a handler for new message events (MESSAGE_CREATED).
        :param commands: List of commands to trigger the handler (optional).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(
                Handler(func, UpdateType.MESSAGE_CREATED, commands, filters)
            )
            return func

        return decorator

    def callback_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for callback events (MESSAGE_CALLBACK).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(
                Handler(func, UpdateType.MESSAGE_CALLBACK, filters=filters)
            )
            return func

        return decorator

    def message_edited_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for edited message events (MESSAGE_EDITED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(Handler(func, UpdateType.MESSAGE_EDITED, filters=filters))
            return func

        return decorator

    def message_removed_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for removed message events (MESSAGE_REMOVED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(Handler(func, UpdateType.MESSAGE_REMOVED, filters=filters))
            return func

        return decorator

    def bot_started_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for bot started events (BOT_STARTED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(Handler(func, UpdateType.BOT_STARTED, filters=filters))
            return func

        return decorator

    def bot_added_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for bot added to chat events (BOT_ADDED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(Handler(func, UpdateType.BOT_ADDED, filters=filters))
            return func

        return decorator

    def bot_removed_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for bot removed from chat events (BOT_REMOVED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(Handler(func, UpdateType.BOT_REMOVED, filters=filters))
            return func

        return decorator

    def user_added_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for user added to chat events (USER_ADDED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(Handler(func, UpdateType.USER_ADDED, filters=filters))
            return func

        return decorator

    def user_removed_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for user removed from chat events (USER_REMOVED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(Handler(func, UpdateType.USER_REMOVED, filters=filters))
            return func

        return decorator

    def chat_title_changed_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for chat title changed events (CHAT_TITLE_CHANGED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(
                Handler(func, UpdateType.CHAT_TITLE_CHANGED, filters=filters)
            )
            return func

        return decorator

    def message_chat_created_handler(self, filters: list[Filter] | None = None):
        """
        Decorator to register a handler for chat created events (MESSAGE_CHAT_CREATED).
        :param filters: List of filters to apply to the update (optional).
        :return: Decorator for the handler function.
        """

        def decorator(func: Callable):
            self.add_handler(
                Handler(func, UpdateType.MESSAGE_CHAT_CREATED, filters=filters)
            )
            return func

        return decorator

    async def polling_loop(self):
        while True:
            try:
                updates = await self.bot.get_updates(
                    timeout=config.DEFAULT_POLLING_TIMEOUT, marker=1
                )
                for update in updates.updates:
                    await self.handle(update)
            except Exception as e:
                logger.error(f"Error in polling loop: {e}")
                await asyncio.sleep(config.DEFAULT_POLLING_TIMEOUT)

    def start_polling(self):
        """
        Start polling for updates from the MAX API and dispatch them to handlers.
        This method runs an infinite loop and should be called in the main entry point.
        """

        asyncio.run(self.polling_loop())
        