from bot_types.base import Model
from bot_types.user_with_photo import UserWithPhoto


class User(Model):
    """
    Represents a user in the system.

    Attributes:
        user_id (int): Unique identifier for the user.
        first_name (str): The user's first name.
        last_name (str | None): The user's last name, if available.
        username (str | None): The user's username, if available.
        is_bot (bool): Indicates whether the user is a bot.
        last_activity_time (int): The Unix timestamp of the user's last activity.
    """

    user_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    is_bot: bool
    last_activity_time: int
