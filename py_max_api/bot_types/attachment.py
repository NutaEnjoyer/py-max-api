from pydantic import Field
from bot_types.base import Model
from bot_types.attachment_type import AttachmentType
from bot_types.photo_attachment_payload import PhotoAttachmentPayload


class Attachment(Model):
    """
    Represents an attachment object containing a specific type and its payload.

    Attributes:
        type_ (AttachmentType): The type of the attachment (e.g., photo, video).
        payload (PhotoAttachmentPayload): The payload data for the attachment.
    """

    type_: AttachmentType = Field(alias="type")
    payload: PhotoAttachmentPayload
