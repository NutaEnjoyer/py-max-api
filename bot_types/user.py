from bot_types.base import Model
from bot_types.user_with_photo import UserWithPhoto


class User(Model):
    user_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    is_bot: bool
    last_activity_time: int
