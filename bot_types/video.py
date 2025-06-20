from .base import Model
from .photo_attachment_payload import PhotoAttachmentPayload
from .video_urls import VideoUrls


class Video(Model):
    token: str
    urls: VideoUrls | None = None
    thumbnail: PhotoAttachmentPayload | None = None
    width: int
    height: int
    duration: int
