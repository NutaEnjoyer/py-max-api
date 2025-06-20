from typing import get_origin, get_args
from pydantic import BaseModel
from methods.base import TelegramMethod
import requests
import logging


logger = logging.getLogger(__name__)


class Session:
    """
    Handles HTTP session and request/response processing for the MAX API bot.
    """

    def __init__(self, bot):
        """
        Initialize the session with a bot instance.
        :param bot: The bot instance using this session.
        """
        self._bot = bot

    def __call__(
        self,
        method: TelegramMethod,
        timeout: int | None = None,
    ):
        """
        Execute an API method with optional timeout and return the parsed response.
        :param method: The API method to execute.
        :param timeout: Optional timeout for the request in seconds.
        :return: Parsed response as a model, list of models, or raw data.
        """
        request = self.generate_request(method)
        prepared = request.prepare()

        with requests.Session() as session:
            response = session.send(prepared, timeout=timeout)
            response.raise_for_status()
            data = response.json()

            model = method.returning
            key = method.key

            if key:
                data = data.get(key)

            logging.info(f"Response: {data}")

            if isinstance(model, type) and issubclass(model, BaseModel):
                return model.model_validate(data)
            elif get_origin(model) is list:
                item_type = get_args(model)[0]
                return [item_type.model_validate(item) for item in data]
            else:
                return data  # fallback for unknown types

    def generate_request(self, method: TelegramMethod) -> requests.Request:
        """
        Generate a requests.Request object for the given API method.
        :param method: The API method to generate a request for.
        :return: A prepared requests.Request object.
        """
        request = requests.Request(
            method=method.type,
            url=self.format_url(method),
            params={**method.params, **self._bot.params},
        )

        if method.headers:
            request.headers = method.headers

        if method.files:
            request.files = method.files
        else:
            request.json = method.body

        return request

    def format_url(self, method: TelegramMethod) -> str:
        """
        Format the full URL for the given API method.
        :param method: The API method to format the URL for.
        :return: The full URL as a string.
        """
        return self._bot.BASE_URL.format(methodName="/" + method.name) + (
            f"/{method.uri}" if method.uri else ""
        )
