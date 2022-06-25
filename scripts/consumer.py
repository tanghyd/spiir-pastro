#!/usr/bin/env python

"""An application to listen to igwn-alert using the hop-client based API."""

import argparse
import json
import logging
import time

from spiir.io.igwn import run_igwn_alert_listener

# initialise logging - to do: implement a more unified logging solution across modules
# https://docs.python.org/3/howto/logging-cookbook.html#multiple-handlers-and-formatters
logger = logging.getLogger("spiir-pastro")
logger.setLevel(logging.DEBUG)

# create file handler that logs debug and higher level messages
fh = logging.FileHandler("out/logs/spiir-pastro.log")  # up one level from bin
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

parser = argparse.ArgumentParser(
    description="Run the SPIIR p(astro) IGWNAlert Consumer."
)
parser.add_argument(
    "-s",
    "--server",
    type=str,
    default="kafka://kafka.scimma.org/",
    help="URL of hop-client server to stream topics from.",
)
parser.add_argument(
    "-g",
    "--group",
    type=str,
    default="gracedb-playground",
    help="Name of GraceDB group",
)
parser.add_argument(
    "-t",
    "--topics",
    type=list[str],
    nargs="+",
    default=["test_spiir"],
    help="IGWN Kafka topics for the listener to subscribe to.",
)
parser.add_argument(
    "--outdir",
    type=str,
    default="../out/results",  # up one level from bin
    help="Output directory to store results.",
)
parser.add_argument(
    "-d",
    "--debug",
    action="store_const",
    dest="loglevel",
    const=logging.DEBUG,
    default=logging.WARNING,
    help="Display all developer debug logging statements",
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_const",
    dest="loglevel",
    const=logging.INFO,
    help="Set logging level to INFO and display progress and information",
)
args = parser.parse_args()
ch.setLevel(level=args.loglevel)  # set console logger handler to specified log level

# verbose = True if args.loglevel <= logging.INFO else False
run_igwn_alert_listener(args.server, args.group, args.topics, args.outdir)
