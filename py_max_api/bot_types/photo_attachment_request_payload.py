from bot_types.base import Model
from typing import Any


class PhotoAttachmentRequestPayload(Model):
    """
    Represents the payload for a photo attachment request.

    Attributes:
        url (str | None): The URL of the photo, if available.
        token (str | None): The token required to access or upload the photo, if available.
        photos (Any | None): Additional photo data or metadata, if available.
    """

    url: str | None = None
    token: str | None = None
    photos: Any | None = None
