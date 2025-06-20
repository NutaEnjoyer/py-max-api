from pydantic import Field
from bot_types.base import Model
from bot_types.message_link_type import MessageLinkType


class NewMessageLink(Model):
    """
    Represents a link to another message, such as for replies or forwards.

    Attributes:
        type_ (MessageLinkType): The type of the message link (e.g., reply or forward).
        mid (str): The unique identifier of the linked message.
    """

    type_: MessageLinkType = Field(alias="type")
    mid: str
