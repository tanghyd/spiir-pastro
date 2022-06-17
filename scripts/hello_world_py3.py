""""A script to compute SPIIR's internal p_astro in Python3.10 ."""
import logging
import time
from pathlib import Path

# from spiir.config.logs import logger

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    while True:
        msg = input()

        # communicate back to py2 via std.out
        time.sleep(0.5)
        print(msg.replace("py2", "py3"))

        if msg == "TERMINATE":
            sys.exit()