import logging
import sys
from src.configuration.configuration import Configuration
from src.configuration.configuration import Configuration

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

if __name__ == "__main__":
    # Should return "Alan Turing"
    random_config_value = Configuration.get_value("RANDOM_CONFIG_KEY")
    logger.info(random_config_value)