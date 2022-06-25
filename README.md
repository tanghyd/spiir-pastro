# SPIIR Astrophysical Source Classification (p_astro)

Author: Daniel Tang [Last Updated: 24/06/22]

We use the PyCBC Mass Contour method for relative astrophysical source classification and a FGMC model (GstLAL) for
a signal vs. noise model.

## Local Installation

We use Python 3.10.4 to make use of the latest typing features for our application.

Additionally, our README refers to the virtual environment name as `venv`, but feel free to replace this with your preferred virtual environment name of choice.

### Conda

Python3.10 installation via conda is straightforward. We can simply install our preferred Python version alongside pip and then simply use pip to install our packages. Note that installing any packages with conda *after* installing with pip may mean that conda cannot find pip installed packages.

    conda create -n venv -c conda-forge python=3.10.4 pip swig m2crypto igwn-alert -y
    conda activate venv
    pip install -r requirements.txt
    pip install -e .  # installs local package

This method was used to install the application virtual environment on CIT - swig and m2crypto must be installed together via conda-forge due to path installation problems with pip.

### Virtualenv

If both Python3.10 and virtualenv is already installed on your machine we can build the virtual environment with the following commands:

    python -m venv venv  # we use python3.10.4
    source venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    pip install -e .  # installs local package

This method was used to install the application virtual environment on OzStar - Python/3.10.4 can be loaded using `module load python/3.10.4`, which comes with swig and m2crypto already compatible with the environment.

Note that it appears that there is no wheel available for confluent_kafka on Python3.10 and so `pip install igwn-alert` will fail on this Kafka dependency. We would recommend downgrading to Python3.9, using Conda, or experiment with installing `confluent-kafka` manually yourself. See: https://github.com/confluentinc/confluent-kafka-python/issues/1219.

### Jupyter Kernel

In order to use this environment in a Jupyter notebook, we can add the virtual environment
to the list of user Jupyter kernels (this works remotely as well).

    python -m ipykernel install --user --name=venv  # consider changing --name

Sometimes issues may arise with some IDEs in remote SSH contexts where the environment is not
immediately added to the list of available kernels. In these instances we recommend resetting
the remote host instance and connecting again. For example the Command Pallete in VSCode
(Cntrl+Shift+P) can be used to Kill VS Sever on Host to force kill the remote instance.

Installed jupyter kernels can be viewed by calling `jupyter kernelspec list`.

## Credentials

### LIGO GraceDb Credentials

TODO: Verify procedure

If `ligo-proxy-utils` are installed, we can generate the appropriate authentication credentials with

Replace albert.einstein with your LIGO username and type your password at the prompt.

    ligo-proxy-init albert.einstein

### SCiMMA Authentication

TODO: Add instructions; see: [SCiMMA Auth](https://my.hop.scimma.org/).

## Developer Guide

### Documentation

All documentation written for this package should follow the [NumPy documentation style guide](https://numpy.org/doc/1.21/docs/howto_document.html), which is a derivation of the Google developer documentation style guide.

<!-- ### Formatting

Black with --line-length 100 . -->

## Current Goals

### Data Collection

- Optimise data extraction from zerolags for efficient data processing (e.g. parquet files, faster LIGO-LW read) [COMPLETE]
- Gather zerolags from 2 week background runs:
  - BBH [COMPLETE]
  - BNS [COMPLETE]
  - NSBH [COMPLETE]
- Gather zerolags from 1 week non-injection runs:
  - BBH [COMPLETE]
  - BNS [COMPLETE]
  - NSBH [COMPLETE]
- Gather zerolags from 1 week injection runs:
  - Generate injection files using lvc_rates_and_pop scripts. [COMPLETE]
  - BBH [COMPLETE]
  - BNS [COMPLETE]
  - NSBH [COMPLETE]
- Extract zerolags and do data pre-processing.
  - Remove contamination of background events from foreground events to discern signal vs. noise.

### Modelling

- Implement PyCBC Live MVP model. [COMPLETE]
- Fit SPIIR's effective distance estimates to BAYESTAR luminosity distances. [COMPLETE]
- Evaluate model performance on injected simulated events. [COMPLETE]
- Evaluate model performance on known merger events (i.e. GWTC). [COMPLETE]
- Implement FGMC model from data collected during SPIIR simulation studies. [IN PROGRESS]
- Improve SPIIR effective distance fit with targeted O3a replay data.
- Implement MC-FGMC model. (Optional)

### Development

- Add NumPy style doc-strings to all functions and classes.
  - Generate documentation with Sphinx.
- Develop [IGWN-Alert](https://git.ligo.org/lscsoft/igwn-alert/-/blob/main/share/igwn_alert_listener) Consumer on CIT systems for p_astro. [COMPLETE]
  - Test deployment of igwn-alert consumer with HTCondor job submission
- Develop internal solution to compute p_astro.json on initial upload without IGWN-Alert. [IN PROGRESS]
- Implement tools to monitor model performance and system state.
- Add GitLab CI/CD Integration.
  - Integrate MLOps tools (e.g. DVC/CML) with GitLab CI/CD. (Optional)
    - Automate data extraction from a remote data repo with DVC.
    - Implement a training test and visualisation for git commits with CML.
