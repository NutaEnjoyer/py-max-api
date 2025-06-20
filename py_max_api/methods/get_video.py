from methods.base import TelegramMethod
from bot_types import Video


class GetVideoMethod(TelegramMethod):
    __returning__ = Video
    __api_method__ = "videos"
    __api_method_type__ = "GET"

    def __init__(
        self,
        video_token: str,
    ):
        super().__init__()
        self.uri = video_token
