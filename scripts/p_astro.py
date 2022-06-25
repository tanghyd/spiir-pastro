""""A script to compute SPIIR's internal p_astro in Python3.10 ."""

import argparse
import json
import logging
import time
from pathlib import Path

import numpy as np

# from spiir.config.logs import logger
from spiir.p_astro import compute_pastro

logger = logging.getLogger()


# def save_json(self, data: dict[str, Any], file_path: Path):
#     with Path(file_path).open(mode="w") as f:
#         f.write(json.dumps(data, indent=4))
#         logger.debug(f"Saved {str(file_path)} to disk")

#     try:
#         gracedb.createVOEvent(graceid, voevent_type="preliminary", **probs)
#         logger.debug(f"{graceid} p_astro.json uploaded to GraceDB")
#     except Exception as e:
#         logger.warning(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the SPIIR p(astro) computation."
    )
    parser.add_argument(
        "--outdir",
        type=str,
        default="../results",
        help="Output directory to store results.",
    )
    # parser.add_argument(
    #     "-d",
    #     "--debug",
    #     action="store_const",
    #     dest="logLevel",
    #     const=logging.DEBUG,
    #     default=logging.WARNING,
    #     help="Display all developer debug logging statements",
    # )
    # parser.add_argument(
    #     "-v",
    #     "--verbose",
    #     action="store_const",
    #     dest="logLevel",
    #     const=logging.INFO,
    #     help="Set logging level to INFO and display progress and information",
    # )
    args = parser.parse_args()
    while True:
        msg = input()

        # communicate back to py2 via std.out
        time.sleep(0.5)

        p_astro = compute_pastro()
        probs = json.dumps(p_astro)
        print(probs)
