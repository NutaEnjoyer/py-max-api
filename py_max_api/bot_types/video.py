from .base import Model
from .photo_attachment_payload import PhotoAttachmentPayload
from .video_urls import VideoUrls


class Video(Model):
    """
    Represents a video object with its metadata and associated resources.

    Attributes:
        token (str): Unique identifier for the video.
        urls (VideoUrls | None): Available URLs for different video resolutions and formats.
        thumbnail (PhotoAttachmentPayload | None): Thumbnail image for the video, if available.
        width (int): Width of the video in pixels.
        height (int): Height of the video in pixels.
        duration (int): Duration of the video in seconds.
    """

    token: str
    urls: VideoUrls | None = None
    thumbnail: PhotoAttachmentPayload | None = None
    width: int
    height: int
    duration: int
