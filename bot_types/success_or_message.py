from pydantic import Field
from .base import Model


class SuccessOrMessage(Model):
    success: bool
    message: str | None = Field(default=None)
