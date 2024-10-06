"""Provider class for in memory config."""

from .abstract_provider import AbstractConfigurationProvider


class InMemoryConfigurationProvider(AbstractConfigurationProvider):
    """Concrete Provider class for In-memory config files."""

    _config: dict

    def __init__(self) -> None:
        self._config = {}

    def get_value(self, key: str):
        """Return the value of the key from the config.

        Args
        ----
            key (str): string representing key to return value for

        Returns
        -------
            value of the key or None
        """
        try:
            return self._config[key]
        except KeyError:
            return None

    def set_value(self, key: str, value: str):
        """Set the value of the config.

        Args
        ----
            key (str): string representing key to return value for

        Returns
        -------
            value of the key or None
        """
        self._config[key] = value
