from bot_types import Updates, UpdateType
from methods.base import TelegramMethod


class GetUpdatesMethod(TelegramMethod):
    __returning__ = Updates
    __api_method__ = "updates"
    __api_method_type__ = "GET"

    def __init__(
        self,
        limit: int | None = None,
        timeout: int | None = None,
        marker: int | None = None,
        types: list[UpdateType] | None = None,
    ):
        super().__init__()

        self.params = {
            "limit": limit,
            "timeout": timeout,
            "marker": marker,
            "types": [type_.value for type_ in types] if types else None,
        }
