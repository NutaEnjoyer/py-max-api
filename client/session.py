from pydantic import BaseModel
from methods.base import TelegramMethod
import requests
import logging


logger = logging.getLogger(__name__)


class Session:
    def __init__(self, bot):
        self._bot = bot

    def __call__(
        self,
        method: TelegramMethod,
        timeout: int | None = None,
    ):
        request = self.generate_request(method, timeout)
        prepared = request.prepare()

        with requests.Session() as session:
            response = session.send(prepared)
            data = response.json()

            model = method.returning
            key = method.key

            print(data)

            if key:
                data = data[key]

            logging.info(f"Response: {data}")

            if isinstance(model, type) and issubclass(model, BaseModel):
                return model.model_validate(data)
            elif hasattr(model, "__origin__") and model.__origin__ is list:
                item_type = model.__args__[0]
                return [item_type.model_validate(item) for item in data]
            else:
                return data  # на крайний случай

    def generate_request(
        self, method: TelegramMethod, timeout: int | None = None
    ) -> requests.Request:
        request = requests.Request(
            method=method.type,
            url=self.format_url(method),
            params={**method.params, **self._bot.params},
        )

        if method.files:
            request.files = method.files
        else:
            request.json = method.body

        if timeout is not None:
            request.timeout = timeout

        return request

    def format_url(self, method: TelegramMethod) -> str:
        return self._bot.BASE_URL.format(methodName="/" + method.name) + (
            f"/{method.uri}" if method.uri else ""
        )
