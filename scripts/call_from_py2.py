#!/usr/bin/env python

import argparse
import ast
import json
import os
import subprocess
import sys
import time
from contextlib import contextmanager

# from spiir.config.logs import logger

@contextmanager
def run_and_terminate_process(*args, **kwargs):
    try:
        p = subprocess.Popen(*args, **kwargs)
        yield p
    finally:
        p.terminate() # send sigterm, or ...
        p.kill()      # send sigkill


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the SPIIR p(astro) computation via subprocess pipe."
    )
    parser.add_argument(
        "-e", "--entry-point",
        type=str,
        default="scripts/local_entrypoint.sh",
        help="Entrypoint bash script for subprocess.",
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
    start = time.clock()
    print("py2: hello world!\n")

    if not os.path.isfile(args.entry_point):
        raise RuntimeError("Entry point script '%s' does not exist." % args.entry_point)

    cmd = ["bash", args.entry_point]

    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    for i in range(3):
        time.sleep(i*0.2)

        msg = "py2: hello #%d" % i
        print(msg)
        try:
            proc.stdin.write(msg + "\n")
        except IOError as e:
            if e.errno == errno.EPIPE or e.errno == errno.EINVAL:
                # Stop loop on "Invalid pipe" or "Invalid argument".
                # No sense in continuing with broken pipe.
                break
            else:
                raise

        out = proc.stdout.readline()
        print("py2: message from py3!")

        print(out)
        p_astro = json.loads(out)

        print(p_astro)

        # [out, err] = proc.communicate(msg)
        # proc.wait()

    # proc.stdin.write("TERMINATE")
    proc.terminate()
    # proc.wait()

    end = time.clock()
    duration = round(end - start, 6)
    print("py2 duration: %.6f" % duration)

    print "Success!"

    # note: if you don't see "Success!" something bad happened
