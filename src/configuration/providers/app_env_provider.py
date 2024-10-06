"""Provider class for environment variables."""

import os

from .abstract_provider import AbstractConfigurationProvider


class AppEnvConfigurationProvider(AbstractConfigurationProvider):
    """Concrete Provider class for os.env."""

    def get_value(self, key: str):
        """Return the value of the key from the os.env.

        Args
        ----
            key (str): string representing key to return value for

        Returns
        -------
            value of the key or None
        """
        return os.getenv(key)