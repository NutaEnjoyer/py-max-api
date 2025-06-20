from typing import Any, Type, get_origin, get_args
from pydantic import BaseModel, Field


class TelegramMethod(BaseModel):
    """
    Base class for all MAX API methods.
    Defines common properties and methods for handling parameters, body, files, and response serialization.
    Child classes should define special attributes (__api_method__, __api_method_type__, __returning__, etc.).
    """

    uri_: str = ""
    params_: dict = Field(default_factory=dict)
    body_: dict = Field(default_factory=dict)
    files_: dict = Field(default_factory=dict)

    @staticmethod
    def serialize(model: type, data: Any):
        """
        Serialize API response data into a pydantic model or a list of models if needed.
        :param model: Model class or typing.List[ModelClass]
        :param data: Data to serialize (dict or list)
        :return: Model instance or list of instances
        """
        if isinstance(model, type) and issubclass(model, BaseModel):
            return model.model_validate(data)
        elif get_origin(model) is list:
            args = get_args(model)
            if args:
                item_type = args[0]
            return [item_type.model_validate(item) for item in data]
        else:
            return data

    @property
    def type(self) -> str:
        """
        HTTP method for the request (GET, POST, PATCH, etc.).
        """
        return getattr(self, "__api_method_type__", "GET")

    @property
    def name(self) -> str:
        """
        API method name (e.g., 'me', 'messages').
        """
        return getattr(self, "__api_method__", "")

    @property
    def params(self) -> dict:
        """
        Query parameters for the request.
        """
        return self.params_

    @params.setter
    def params(self, value: dict):
        """
        Set query parameters for the request.
        """
        self.params_ = value

    @property
    def returning(self) -> Type[BaseModel] | None:
        """
        Model class that the method should return (or None).
        """
        return getattr(self, "__returning__", None)

    @property
    def key(self) -> str | None:
        """
        Key in the API response to extract data from (if any).
        """
        return getattr(self, "__return_key__", None)

    @property
    def body(self) -> dict:
        """
        Request body.
        """
        return self.body_

    @body.setter
    def body(self, value):
        """
        Set request body.
        """
        self.body_ = value

    @property
    def files(self) -> dict:
        """
        Files for multipart/form-data requests.
        """
        return self.files_

    @files.setter
    def files(self, value):
        """
        Set files for multipart/form-data requests.
        """
        self.files_ = value

    @property
    def uri(self) -> str:
        """
        URI part for the method (e.g., chat_id for /chats/{chat_id}).
        """
        return self.uri_

    @uri.setter
    def uri(self, value):
        """
        Set URI part for the method.
        """
        self.uri_ = value

    @property
    def headers(self) -> dict | None:
        """
        Headers for the request (if required by the method).
        """
        return getattr(self, "__headers__", None)
