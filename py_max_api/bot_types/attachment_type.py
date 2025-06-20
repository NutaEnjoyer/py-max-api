from enum import Enum


class AttachmentType(str, Enum):
    """
    Enum representing the different types of attachments that can be used in the bot.

    Attributes:
        IMAGE: Represents an image attachment.
        VIDEO: Represents a video attachment.
        AUDIO: Represents an audio attachment.
        FILE: Represents a generic file attachment.
        STICKER: Represents a sticker attachment.
        CONTACT: Represents a contact attachment.
        INLINE_KEYBOARD: Represents an inline keyboard attachment.
        SHARE: Represents a share attachment.
        LOCATION: Represents a location attachment.
    """

    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    STICKER = "sticker"
    CONTACT = "contact"
    INLINE_KEYBOARD = "inline_keyboard"
    SHARE = "share"
    LOCATION = "location"
