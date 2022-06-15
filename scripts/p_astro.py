#!/usr/bin/env python

""""An application to upload p_astro.json to GraceDB."""

import argparse
import json
import logging
import time
from pathlib import Path

import numpy as np
from ligo.gracedb.rest import GraceDb
# from spiir.config.logs import logger
from spiir.search.p_astro import compute_pastro

logger = logging.getLogger()


# def save_json(self, data: dict[str, Any], file_path: Path):
#     with Path(file_path).open(mode="w") as f:
#         f.write(json.dumps(data, indent=4))
#         logger.debug(f"Saved {str(file_path)} to disk")


def upload_pastro(gracedb: GraceDb, graceid: str, probs: dict[str, float]):
    assert gracedb is not None
    for key in ("BNS", "NSBH", "BBH", "Terrestrial"):
        assert key in probs, f"{key} not present in {list(probs.keys())}"

    try:
        gracedb.createVOEvent(graceid, voevent_type="preliminary", **probs)
        logger.debug(f"{graceid} p_astro.json uploaded to GraceDB")
    except Exception as e:
        logger.warning(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the SPIIR p(astro) computation."
    )
    parser.add_argument(
        "-g",
        "--group",
        type=str,
        default="gracedb-playground",
        help="Name of GraceDB group",
    )
    # parser.add_argument(
    #     "--service-url",
    #     type=str,
    #     default="https://gracedb-playground.ligo.org/api/",
    #     help="GraceDB upload API URL."
    # )
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

    # verbose = True if args.loglevel <= logging.INFO else False

    # instantiate GraceDb client
    gracedb_groups = {"gracedb", "gracedb-test", "gracedb-playground"}
    if args.group not in gracedb_groups:
        raise KeyError(f"Provided {args.group} not one of {gracedb_groups}.")
    service_url = f"https://{args.group}.ligo.org/api/"
    logger.info(f"service_url: {service_url}")
    
    try:
        gracedb = GraceDb(service_url=service_url, reload_certificate=True)
        logger.info(f"Initialised GraceDB connection at {service_url}")
    except Exception as e:
        logger.warning(e)

    # compute p_astro
    start = time.perf_counter()
    p_astro = compute_pastro()
    end = time.perf_counter()

    duration = round(end - start, 4)
    logger.info(f"py3 duration: {duration}")

    # communicate back to py2 via std.out
    print(p_astro)
