from bot_types import Me
from methods.base import TelegramMethod


class GetMeMethod(TelegramMethod):

    __returning__ = Me
    __api_method__ = "me"
    __api_method_type__ = "GET"
