"""Module to provide an instance of the configuration."""

import os
from typing import Any
from pathlib import Path

from src.configuration.providers.abstract_provider import AbstractConfigurationProvider
from src.configuration.providers.app_env_provider import AppEnvConfigurationProvider
from src.configuration.providers.json_provider import JsonConfigurationProvider
from src.configuration.providers.in_memory_provider import InMemoryConfigurationProvider
from src.configuration.providers.keyvault_provider import KeyVaultConfigurationProvider

class ConfigurationError(Exception):
    """An error raised when there is an issue with the configuration."""

class Configuration:
    """Utility class to return all config values."""

    _providers: Any = None
    _in_memory_provider = InMemoryConfigurationProvider()

    @staticmethod
    def initialize():
        """Initialize default providers.

        Returns
        -------
            an instance of the class
        """
        if Configuration._providers is None:
            json_config_file_path = Path(__file__).parent / "config.json"
            Configuration._providers = []
            Configuration._providers.append(Configuration._in_memory_provider)
            Configuration._providers.append(AppEnvConfigurationProvider())
            Configuration._providers.append(JsonConfigurationProvider(json_config_file_path))
            kv_name = Configuration.get_value(key="KEYVAULT_NAME", nullable=True)
            if kv_name is not None:
                Configuration._providers.append(KeyVaultConfigurationProvider(kv_name))

    @staticmethod
    def register_provider(provider: AbstractConfigurationProvider):
        """Prepend a provider to the list of providers.

        Args
        ----
            provider(AbstractConfigurationProvider): an instance of the provider
        """
        Configuration.initialize()
        Configuration._providers.insert(0, provider)

    @staticmethod
    def set_value(key: str, value: str):
        """Set a config value in memory.

        Args
        ----
            key (str): the config key
            value (str): the value for the key
        """
        Configuration._in_memory_provider.set_value(key, value)

    @staticmethod
    def get_value(key: str, nullable=False):
        """Return the value of the key from any of the providers.

        Args
        ----
            key (str): a string containing the key
            nullable (bool): to return none if value is not found or throw exception

        Raises
        ------
            Exception: exception if key is not found

        Returns
        -------
            the value of the key
        """
        Configuration.initialize()
        value = None
        # pylint: disable=not-an-iterable
        for provider in Configuration._providers:
            value = provider.get_value(key)
            if value is not None:
                return value
        if nullable:
            return None
        
        raise ConfigurationError(f"Config value does not exist for {key}")