#!/bin/bash

module purge

module load gcc/9.2.0 openmpi/4.0.2
module load python/3.10.4
. ../spiir-pastro/venv/bin/activate
python ../spiir-pastro/scripts/p_astro.py