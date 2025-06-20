from bot_types.base import Model
from bot_types.user import User
from bot_types.recipient import Recipient
from bot_types.linked_message import LinkedMessage
from bot_types.message_body import MessageBody
from bot_types.message_stat import MessageStat
from pydantic import computed_field


class Message(Model):
    """
    Represents a message entity.

    Attributes:
        sender (User): The user who sent the message.
        recipient (Recipient): The recipient of the message.
        timestamp (int): The timestamp when the message was sent (in Unix time).
        link (LinkedMessage | None): Information about a linked message (e.g., reply or forward), if any.
        body (MessageBody): The body of the message, including text, attachments, and markup.
        stat (MessageStat | None): Statistics related to the message, such as views, if available.
        url (str | None): A URL to the message, if available.
    """

    sender: User
    recipient: Recipient
    timestamp: int
    link: LinkedMessage | None = None
    body: MessageBody
    stat: MessageStat | None = None
    url: str | None = None

    @computed_field
    def message_id(self) -> str:
        """
        Returns the unique message identifier.

        Returns:
            str: The message ID.
        """
        return self.body.mid

    @computed_field
    def text(self) -> str | None:
        """
        Returns the text content of the message, if any.

        Returns:
            str | None: The text of the message, or None if not present.
        """
        return self.body.text
