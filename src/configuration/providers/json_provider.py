"""Provider class for JSON File variables."""

import logging
import json
import logging
from json import JSONDecodeError
from pathlib import Path

from .abstract_provider import AbstractConfigurationProvider

class JsonConfigurationProvider(AbstractConfigurationProvider):
    """Concrete Provider class for JSON files, can be extended by derivation."""

    def __init__(self, file_path: str):
        self.logger = logging.getLogger(__name__)
        self.file_contents = self._load_configuration(file_path)

    def get_value(self, key: str):
        """Get value."""
        if key in self.file_contents:
            return self.file_contents[key]
        return None

    def _load_configuration(self, file_path: str) -> dict:
        """Load JSON Configuration."""

        if not Path(file_path).exists():
            self.logger.error("JSON configuration file not found: %s", file_path)
            raise FileNotFoundError(f"JSON configuration file not found: {file_path}")

        try:
            with Path(file_path).open("r") as config_file:
                return json.load(config_file)
        except JSONDecodeError:
            self.logger.exception(
                "JSON decoding error for configuration file %s", file_path
            )
            raise