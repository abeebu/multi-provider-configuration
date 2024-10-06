"""Abstract class for configuration providers."""

from abc import ABC
from abc import abstractmethod


class AbstractConfigurationProvider(ABC):
    """Abstract Provider class for configurations."""

    @abstractmethod
    def get_value(self, key: str):
        """Abstract method for all providers.

        Args
        ----
            key (str): string representing key to return value for
        """
        pass