from pydantic import Field
from bot_types.base import Model
from bot_types.attachment_type import AttachmentType
from bot_types.photo_attachment_request_payload import PhotoAttachmentRequestPayload


class AttachmentRequest(Model):
    """
    Represents a request for an attachment.

    Attributes:
        type_ (AttachmentType): The type of the attachment. This field is aliased as "type" in the serialized output.
        payload (PhotoAttachmentRequestPayload): The payload containing details specific to the photo attachment request.
    """

    type_: AttachmentType = Field(alias="type")
    payload: PhotoAttachmentRequestPayload
