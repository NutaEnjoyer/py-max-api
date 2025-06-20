from enum import Enum


class UpdateType(str, Enum):
    """
    Enum representing the types of updates that can occur in the bot system.

    Attributes:
        MESSAGE_CREATED: Indicates that a new message was created.
        MESSAGE_CALLBACK: Indicates that a callback from a message was received (e.g., button press).
        MESSAGE_EDITED: Indicates that an existing message was edited.
        MESSAGE_REMOVED: Indicates that a message was removed.
        BOT_ADDED: Indicates that the bot was added to a chat.
        BOT_REMOVED: Indicates that the bot was removed from a chat.
        USER_ADDED: Indicates that a user was added to a chat.
        USER_REMOVED: Indicates that a user was removed from a chat.
        BOT_STARTED: Indicates that the bot was started.
        CHAT_TITLE_CHANGED: Indicates that the chat title was changed.
        MESSAGE_CHAT_CREATED: Indicates that a new chat was created via a message.
    """

    MESSAGE_CREATED = "message_created"
    MESSAGE_CALLBACK = "message_callback"
    MESSAGE_EDITED = "message_edited"
    MESSAGE_REMOVED = "message_removed"
    BOT_ADDED = "bot_added"
    BOT_REMOVED = "bot_removed"
    USER_ADDED = "user_added"
    USER_REMOVED = "user_removed"
    BOT_STARTED = "bot_started"
    CHAT_TITLE_CHANGED = "chat_title_changed"
    MESSAGE_CHAT_CREATED = "message_chat_created"
