from pydantic import Field
from bot_types.base import Model


class BotCommand(Model):
    """
    Represents a command that can be used in the bot.

    Attributes:
        name (str): The name of the command.
        description (str | None): The description of the command.
    """

    name: str = Field(max_length=64)
    description: str | None = Field(max_length=128, default=None)
