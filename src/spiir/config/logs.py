import logging
import logging.config
from pathlib import Path

# specify logging.ini path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
LOGGING_CONFIG = ROOT_DIR / "config" / "logging.ini"

if LOGGING_CONFIG.is_file():
    # load logging configuration
    logging.config.fileConfig(LOGGING_CONFIG)
    logger = logging.getLogger()
    logger.info(f"Loaded logging configuration from {LOGGING_CONFIG}.")

    # create output folder for file logs
    # TODO:
    #   - condition on whether a file handler exists in the logging config
    #   - be able to specify output log directory paths (LOGGING_CONFIG and logs_dir)
    logs_dir = ROOT_DIR / "logs"
    logs_dir.mkdir(exist_ok=True)
    logger.info(f"File logs being output to {logs_dir}")
else:
    # should there be a default alternative if logging.ini is not present?
    raise FileNotFoundError(f"{LOGGING_CONFIG} not found.")
