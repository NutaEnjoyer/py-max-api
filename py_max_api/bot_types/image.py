from bot_types.base import Model


class Image(Model):
    """
    Represents an image with a URL.

    Attributes:
        url (str): The URL of the image.
    """

    url: str
