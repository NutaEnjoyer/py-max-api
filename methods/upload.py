from methods.base import TelegramMethod
from bot_types.photo_attachment_request_payload import PhotoAttachmentRequestPayload
from bot_types.upload import Upload
from bot_types.upload_type import UploadType


class UploadMethod(TelegramMethod):
    __returning__ = Upload
    __api_method__ = "uploads"
    __api_method_type__ = "POST"
    __headers__ = {
        "Content-Type": "multipart/form-data",
    }

    def __init__(self, path: str, type_: UploadType):
        super().__init__()
        self.body = {"type": type_.value}
        self.files = {"data": (path, open(path, "rb"), "image/png")}
