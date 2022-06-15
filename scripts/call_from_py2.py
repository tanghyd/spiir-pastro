#!/usr/bin/env python

import ast
import os
import subprocess
import sys
import time

# from spiir.config.logs import logger


if __name__ == "__main__":
    start = time.clock()
    print("hello py2")


    # cmd = ["../spiir-pastro/venv/bin/python", "../spiir-pastro/scripts/p_astro.py"]
    cmd = ["bash", "../spiir-pastro/scripts/run_p_astro_subprocess.sh"]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    [out, err] = proc.communicate()

    if out:
        print("out: %s" % out)
        p_astro = ast.literal_eval(out)
            
        for key in p_astro:
            print(key, p_astro[key])

        total = sum(float(p_astro[key]) for key in p_astro)
        print(total)
        
    if err:
        print("err: %s" % err)



    end = time.clock()
    duration = round(end - start, 6)
    print("py2 duration: %.6f" % duration)

    print "Success!"

    # note: if you don't see "Success!" something bad happened