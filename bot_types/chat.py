from pydantic import Field
from bot_types.base import Model
from bot_types.chat_type import ChatType
from bot_types.chat_status import ChatStatus
from bot_types.user import User
from bot_types.image import Image
from bot_types.user_with_photo import UserWithPhoto
from bot_types.message import Message


class Chat(Model):
    chat_id: int
    type_: ChatType = Field(alias="type")
    status: ChatStatus
    title: str | None = None
    icon: Image | None = None
    last_event_time: int
    owner_id: int | None = None
    participants: list[User] | None = None
    is_public: bool
    link: str | None = None
    description: str | None = None
    dialog_with_user: UserWithPhoto | None = None
    message_count: int | None = None
    chat_message_id: str | None = None
    pinned_message: Message | None = None
