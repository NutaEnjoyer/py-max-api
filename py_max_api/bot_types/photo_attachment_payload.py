from bot_types.base import Model


class PhotoAttachmentPayload(Model):
    """
    Represents the payload for a photo attachment.

    Attributes:
        photo_id (str): The unique identifier of the photo.
        token (str): The token required to access or upload the photo.
        url (str): The URL of the photo.
    """

    photo_id: str
    token: str
    url: str
