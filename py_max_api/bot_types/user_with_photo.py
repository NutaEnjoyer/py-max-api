from bot_types.base import Model


class UserWithPhoto(Model):
    """
    Represents a user with additional photo information.

    Attributes:
        user_id (int): Unique identifier for the user.
        first_name (str): The user's first name.
        last_name (str | None): The user's last name, if available.
        username (str | None): The user's username, if available.
        is_bot (bool): Indicates whether the user is a bot.
        last_activity_time (int): The Unix timestamp of the user's last activity.
        description (str | None): The user's description or bio, if available.
        avatar_url (str | None): URL to the user's avatar image, if available.
        full_avatar_url (str | None): URL to the user's full-size avatar image, if available.
    """

    user_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    is_bot: bool
    last_activity_time: int
    description: str | None = None
    avatar_url: str | None = None
    full_avatar_url: str | None = None
