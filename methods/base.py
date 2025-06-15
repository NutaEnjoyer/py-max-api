from pydantic import BaseModel, Field


class TelegramMethod(BaseModel):
    uri_: str = ""
    params_: dict = Field(default_factory=dict)
    body_: dict = Field(default_factory=dict)
    files_: dict = Field(default_factory=dict)

    @staticmethod
    def serialize(model: BaseModel, data: any):
        if isinstance(model, type) and issubclass(model, BaseModel):
            return model.model_validate(data)
        elif hasattr(model, "__origin__") and model.__origin__ is list:
            item_type = model.__args__[0]
            return [item_type.model_validate(item) for item in data]
        else:
            return data

    @property
    def type(self) -> str:
        """
        Method type
        """
        return self.__api_method_type__

    @property
    def name(self) -> str:
        """
        Method name
        """
        return self.__api_method__

    @property
    def params(self) -> dict:
        """
        Method params
        """
        return self.params_

    @params.setter
    def params(self, value: dict):
        self.params_ = value

    @property
    def returning(self) -> type:
        """
        Return type
        """
        return self.__returning__

    @property
    def key(self) -> str | None:
        """
        Return key
        """
        return getattr(self, "__return_key__", None)

    @property
    def body(self) -> dict:
        """
        Return body
        """
        return self.body_

    @body.setter
    def body(self, value):
        self.body_ = value

    @property
    def files(self) -> dict:
        """
        Return files
        """
        return self.files_

    @files.setter
    def files(self, value):
        self.files_ = value

    @property
    def uri(self) -> str:
        """
        Return uri
        """
        return self.uri_

    @uri.setter
    def uri(self, value):
        self.uri_ = value
