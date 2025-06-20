from pydantic import Field
from .base import Model


class SuccessOrMessage(Model):
    """
    Represents a response that indicates either a success status or an optional message.

    Attributes:
        success (bool): Indicates whether the operation was successful.
        message (str | None): An optional message providing additional information about the result.
    """

    success: bool
    message: str | None = Field(default=None)
