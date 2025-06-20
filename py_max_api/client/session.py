"""
This module provides the Session class for handling HTTP requests to the MAX API.
Supports both synchronous and asynchronous request handling.
"""

from typing import get_origin, get_args
from pydantic import BaseModel
from methods.base import TelegramMethod
import aiohttp
import logging
import asyncio

logger = logging.getLogger(__name__)

class Session:
    """
    Handles HTTP session and request/response processing for the MAX API bot.
    Supports both synchronous and asynchronous request handling.
    """
    def __init__(self, bot):
        """
        Initialize the session with a bot instance.
        :param bot: The bot instance using this session.
        """
        self._bot = bot

    async def __call__(
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
        request_data = self.generate_request_data(method)
        
        timeout_obj = aiohttp.ClientTimeout(total=timeout) if timeout else None
        
        async with aiohttp.ClientSession(timeout=timeout_obj) as session:
            async with session.request(
                method=method.type,
                url=request_data['url'],
                params=request_data['params'],
                headers=request_data['headers'],
                json=request_data['json'],
                data=request_data['data']
            ) as response:
                response.raise_for_status()
                data = await response.json()

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

    def generate_request_data(self, method: TelegramMethod) -> dict:
        """
        Generate request data for the given API method.
        :param method: The API method to generate request data for.
        :return: Dictionary containing URL, params, headers, json, and data.
        """
        url = self.format_url(method)
        params = {k: v for k, v in {**method.params, **self._bot.params}.items() if v is not None}
        headers = method.headers or {}
        
        # Handle files and body
        json_data = None
        form_data = None
        
        if method.files:
            # For file uploads, use FormData
            form_data = aiohttp.FormData()
            for key, file_info in method.files.items():
                if isinstance(file_info, tuple) and len(file_info) >= 2:
                    file_path = file_info[0]
                    content_type = file_info[2] if len(file_info) > 2 else None
                    with open(file_path, 'rb') as f:
                        form_data.add_field(key, f, filename=file_path, content_type=content_type)
        else:
            json_data = method.body

        return {
            'url': url,
            'params': params,
            'headers': headers,
            'json': json_data,
            'data': form_data
        }

    def format_url(self, method: TelegramMethod) -> str:
        """
        Format the full URL for the given API method.
        :param method: The API method to format the URL for.
        :return: The full URL as a string.
        """
        return self._bot.BASE_URL.format(methodName="/" + method.name) + (
            f"/{method.uri}" if method.uri else ""
        )

    # Synchronous wrapper for backward compatibility
    def __call__sync(
        self,
        method: TelegramMethod,
        timeout: int | None = None,
    ):
        """
        Synchronous wrapper for the async __call__ method.
        :param method: The API method to execute.
        :param timeout: Optional timeout for the request in seconds.
        :return: Parsed response as a model, list of models, or raw data.
        """
        return asyncio.run(self.__call__(method, timeout))
