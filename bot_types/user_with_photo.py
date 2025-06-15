from bot_types.base import Model


class UserWithPhoto(Model):
    user_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    is_bot: bool
    last_activity_time: int
    description: str | None = None
    avatar_url: str | None = None
    full_avatar_url: str | None = None
