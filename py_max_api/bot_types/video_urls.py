from bot_types.base import Model


class VideoUrls(Model):
    """
    Represents different available video URLs for various resolutions and formats.

    Attributes:
        mp4_1080 (str | None): URL to the 1080p MP4 video, if available.
        mp4_720 (str | None): URL to the 720p MP4 video, if available.
        mp4_480 (str | None): URL to the 480p MP4 video, if available.
        mp4_360 (str | None): URL to the 360p MP4 video, if available.
        mp4_240 (str | None): URL to the 240p MP4 video, if available.
        mp4_144 (str | None): URL to the 144p MP4 video, if available.
        hls (str | None): URL to the HLS (HTTP Live Streaming) video, if available.
    """

    mp4_1080: str | None = None
    mp4_720: str | None = None
    mp4_480: str | None = None
    mp4_360: str | None = None
    mp4_240: str | None = None
    mp4_144: str | None = None
    hls: str | None = None
