from pydantic import Field
from bot_types.base import Model
from bot_types.message_link_type import MessageLinkType
from bot_types.user import User
from bot_types.message_body import MessageBody


class LinkedMessage(Model):
    """
    Represents a message that is linked to another message or entity.

    Attributes:
        message_type (MessageLinkType): The type of the linked message, aliased as "type".
        sender (User): The user who sent the message.
        chat_id (int | None): The ID of the chat where the message was sent. Can be None.
        message (MessageBody): The body of the linked message.
    """

    message_type: MessageLinkType = Field(alias="type")
    sender: User
    chat_id: int | None = None
    message: MessageBody
