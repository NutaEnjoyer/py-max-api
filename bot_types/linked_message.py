from pydantic import Field
from bot_types.base import Model
from bot_types.message_link_type import MessageLinkType
from bot_types.user import User
from bot_types.message_body import MessageBody


class LinkedMessage(Model):
    message_type: MessageLinkType = Field(alias="type")
    sender: User
    chat_id: int | None = None
    message: MessageBody
