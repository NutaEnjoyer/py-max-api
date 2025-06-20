from bot_types.base import Model


class Upload(Model):
    """
    Represents an uploaded file.

    Attributes:
        url (str): The URL where the uploaded file can be accessed.
    """

    url: str
