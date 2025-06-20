from bot_types.base import Model


class VideoUrls(Model):
    mp4_1080: str | None = None
    mp4_720: str | None = None
    mp4_480: str | None = None
    mp4_360: str | None = None
    mp4_240: str | None = None
    mp4_144: str | None = None
    hls: str | None = None
