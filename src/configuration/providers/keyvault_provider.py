"""Provider class for KeyVault variables."""

from azure.core.exceptions import ResourceNotFoundError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from .abstract_provider import AbstractConfigurationProvider


class KeyVaultConfigurationProvider(AbstractConfigurationProvider):
    """Concrete Provider class for KeyVault."""

    kv_uri: str
    config: dict = {}

    def __init__(self, name: str) -> None:
        """Initialize the class.

        Args
        ----
            name (str): name of the KeyVault
        """
        self.kv_uri = f"https://{name}.vault.azure.net"

    def get_value(self, key: str):
        """Retrieve the value of the secret given the key.

        Args
        ----
            key (str): a string representing the secret key

        Returns
        -------
            the value of the secret or None if no value is found
        """
        try:
            if key in self.config:
                return self.config[key]
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=self.kv_uri, credential=credential)
            value = client.get_secret(key).value
            self.config[key] = value
            return value
        except ResourceNotFoundError:
            return None