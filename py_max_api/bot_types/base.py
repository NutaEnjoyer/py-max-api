from pydantic import BaseModel


class Model(BaseModel):
    """
    Base model class for all data models in the bot_types package.

    Inherits from pydantic.BaseModel and provides a custom string
    representation using JSON serialization.
    """

    def __str__(self):
        """
        Return a JSON string representation of the model instance.
        """
        return self.model_dump_json()
