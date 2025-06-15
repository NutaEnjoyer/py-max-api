from bot_types.base import Model
from bot_types.bot_command import BotCommand


class Me(Model):
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
