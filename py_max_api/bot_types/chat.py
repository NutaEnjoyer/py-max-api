from pydantic import Field
from bot_types.base import Model
from bot_types.chat_type import ChatType
from bot_types.chat_status import ChatStatus
from bot_types.user import User
from bot_types.image import Image
from bot_types.user_with_photo import UserWithPhoto
from bot_types.message import Message


class Chat(Model):
    """
    Represents a chat entity with various attributes such as type, status, participants, and more.
    """

    chat_id: int
    """Unique identifier for the chat."""

    type_: ChatType = Field(alias="type")
    """Type of the chat (e.g., group, private, channel)."""

    status: ChatStatus
    """Current status of the chat."""

    title: str | None = None
    """Title of the chat, if applicable."""

    icon: Image | None = None
    """Icon image of the chat, if available."""

    last_event_time: int
    """Timestamp of the last event in the chat (in Unix time)."""

    owner_id: int | None = None
    """User ID of the chat owner, if applicable."""

    participants: list[User] | None = None
    """List of users participating in the chat."""

    is_public: bool
    """Indicates whether the chat is public."""

    link: str | None = None
    """Public link to the chat, if available."""

    description: str | None = None
    """Description of the chat."""

    dialog_with_user: UserWithPhoto | None = None
    """User information for private dialogs, if applicable."""

    message_count: int | None = None
    """Total number of messages in the chat."""

    chat_message_id: str | None = None
    """Identifier of a specific message in the chat, if relevant."""

    pinned_message: Message | None = None
    """The pinned message in the chat, if any."""
