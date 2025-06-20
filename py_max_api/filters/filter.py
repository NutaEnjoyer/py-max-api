from bot_types import Update
from abc import ABC, abstractmethod


class Filter(ABC):
    """
    Abstract base class for all filters.

    Subclasses should implement the check method to determine
    whether a given update passes the filter.
    """

    @abstractmethod
    def check(self, update: Update) -> bool:
        """
        Check whether the given update passes the filter.

        Args:
            update (Update): The update to check.

        Returns:
            bool: True if the update passes the filter, False otherwise.
        """
        ...
