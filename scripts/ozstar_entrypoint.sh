#!/bin/bash

# default spiir python path
# echo "SPIIR PYTHONPATH: ${PYTHONPATH}"

# entirely wipe PYTHONPATH because some spiir python dependencies cause issues
export PYTHONPATH=""
# echo "EMPTY PYTHONPATH: ${PYTHONPATH}"


# load modules for spiir-pastro in python-3.10.4
module purge
module load gcc/9.2.0 openmpi/4.0.2
module load cudnn/8.1.0-cuda-11.2.0
module load git/2.18.0
module load python/3.10.4
# echo "P-ASTRO PYTHONPATH: ${PYTHONPATH}"

bash scripts/run_p_astro_subprocess.sh