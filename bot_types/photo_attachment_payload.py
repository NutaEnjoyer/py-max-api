from bot_types.base import Model


class PhotoAttachmentPayload(Model):
    photo_id: str
    token: str
    url: str
