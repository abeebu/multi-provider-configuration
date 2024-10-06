import logging
from src.configuration.configuration import Configuration
from src.configuration.configuration import Configuration

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Should return "Alan Turing"
    random_config_value = Configuration.get_value("RANDOM_CONFIG_KEY")
    print(random_config_value)
    logger.info(random_config_value)