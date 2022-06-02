import logging

from spiir.config.logs import logger

# logger = logging.getLogger()


if __name__ == "__main__":
    print("hello")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
    print("program complete")