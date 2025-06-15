from bot_types.base import Model
from bot_types.chat_type import ChatType


class Recipient(Model):
    chat_id: int
    chat_type: ChatType
    user_id: int | None = None
