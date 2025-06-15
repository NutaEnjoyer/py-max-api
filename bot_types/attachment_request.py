from pydantic import Field
from bot_types.base import Model
from bot_types.attachment_type import AttachmentType
from bot_types.photo_attachment_request_payload import PhotoAttachmentRequestPayload


class AttachmentRequest(Model):
    type_: AttachmentType = Field(alias="type")
    payload: PhotoAttachmentRequestPayload
