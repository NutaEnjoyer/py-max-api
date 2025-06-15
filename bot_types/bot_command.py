from pydantic import Field
from bot_types.base import Model


class BotCommand(Model):
    name: str = Field(max_length=64)
    description: str | None = Field(max_length=128, default=None)
