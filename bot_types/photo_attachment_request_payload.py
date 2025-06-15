from bot_types.base import Model
from typing import Any


class PhotoAttachmentRequestPayload(Model):
    url: str | None = None
    token: str | None = None
    photos: Any | None = None
