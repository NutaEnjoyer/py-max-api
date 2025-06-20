from bot_types.base import Model
from bot_types.bot_command import BotCommand


class Me(Model):
    """
    Represents the current bot or user.

    Attributes:
        user_id (int): Unique identifier for the user or bot.
        first_name (str): First name of the user or bot.
        last_name (str | None): Last name of the user or bot, if available.
        username (str | None): Username of the user or bot, if available.
        last_activity_time (int): Timestamp of the last activity (in Unix time).
        is_bot (bool): Indicates whether this entity is a bot.
        description (str | None): Description or bio of the user or bot, if available.
        avatar_url (str | None): URL to the avatar image, if available.
        full_avatar_url (str | None): URL to the full-size avatar image, if available.
        commands (list[BotCommand] | None): List of bot commands available to this bot, if any.
    """

    user_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    last_activity_time: int
    is_bot: bool
    description: str | None = None
    avatar_url: str | None = None
    full_avatar_url: str | None = None
    commands: list[BotCommand] | None = None
