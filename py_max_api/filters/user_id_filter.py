from .filter import Filter
from bot_types import Update


class UserIdFilter(Filter):
    """
    Filter that checks if the sender's user_id matches the specified user_id(s).
    """

    def __init__(self, user_id: int | list[int]):
        """
        Initialize the UserIdFilter.

        Args:
            user_id (int | list[int]): A single user_id or a list of user_ids to filter messages by.
        """
        super().__init__()
        self.user_id = user_id

    def check(self, update: Update) -> bool:
        """
        Check if the sender's user_id matches the filter.

        Args:
            update (Update): The update object containing the message.

        Returns:
            bool: True if the sender's user_id matches, False otherwise.
        """
        if isinstance(self.user_id, list):
            return update.message.sender.user_id in self.user_id
        else:
            return update.message.sender.user_id == self.user_id
