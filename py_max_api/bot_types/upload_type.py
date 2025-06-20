from enum import Enum


class UploadType(str, Enum):
    """
    Enum representing the types of uploads supported by the bot.

    Attributes:
        IMAGE: Represents an image upload.
        VIDEO: Represents a video upload.
        AUDIO: Represents an audio upload.
        FILE: Represents a generic file upload.
    """

    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
