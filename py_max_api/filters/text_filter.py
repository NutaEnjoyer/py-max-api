from bot_types import Update
from .filter import Filter


class TextFilter(Filter):
    """
    Filter for checking if a message text matches a specific string, list of strings, or starts with a given prefix.

    Args:
        text (str | list[str] | None): The text or list of texts to match exactly. Mutually exclusive with 'startswith'.
        startswith (str | None): The prefix to check if the message text starts with. Mutually exclusive with 'text'.

    Raises:
        ValueError: If both 'text' and 'startswith' are provided, or if neither is provided.
    """

    def __init__(
        self,
        text: str | list[str] | None = None,
        startswith: str | None = None,
    ):
        """
        Initialize the TextFilter.

        Args:
            text (str | list[str] | None): The text or list of texts to match exactly.
            startswith (str | None): The prefix to check if the message text starts with.

        Raises:
            ValueError: If both 'text' and 'startswith' are provided, or if neither is provided.
        """
        super().__init__()
        if text and startswith:
            raise ValueError("text and startswith cannot be used together")

        if not text and not startswith:
            raise ValueError("text or startswith must be provided")

        self.text = text
        self.startswith = startswith

    def check(self, update: Update) -> bool:
        """
        Check if the update's message text matches the filter criteria.

        Args:
            update (Update): The update object containing the message.

        Returns:
            bool: True if the message text matches the filter, False otherwise.
        """
        if self.text:
            if isinstance(self.text, list):
                return update.message.text in self.text
            else:
                return update.message.text == self.text
        else:
            # if startswith is not None
            return update.message.text.startswith(self.startswith)
