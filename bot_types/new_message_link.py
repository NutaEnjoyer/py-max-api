from pydantic import Field
from bot_types.base import Model
from bot_types.message_link_type import MessageLinkType


class NewMessageLink(Model):
    type_: MessageLinkType = Field(alias="type")
    mid: str
