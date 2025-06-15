from bot_types.base import Model
from bot_types.user import User
from bot_types.recipient import Recipient
from bot_types.linked_message import LinkedMessage
from bot_types.message_body import MessageBody
from bot_types.message_stat import MessageStat


class Message(Model):
    sender: User
    recipient: Recipient
    timestamp: int
    link: LinkedMessage | None = None
    body: MessageBody
    stat: MessageStat | None = None
    url: str | None = None
