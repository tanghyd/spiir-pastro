# SPIIR Astrophysical Source Classification (p_astro)

Author: Daniel Tang

Last Updated: 01/06/22

## Introduction

We use the PyCBC Mass Contour method for relative astrophysical source classification and a FGMC model (GstLAL) for
a signal vs. noise model.

## Setup

### Installation

Basic installation commands used to install the virtual environment are as follows:

    python -m venv venv                 # we use python3.7.4
    source venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt 

## Current Goals

### Data

- Optimise data extraction from zerolags for efficient modelling (mulitprocessing, big data file formats)
  - Specify source data directory/ies and extract them from .xml.gz (LIGO-LW) formats to data/staging
  - Handle data transformation and aggregation into optimised file types to data/processed (such as .parquet, .h5 etc.)
- Gather foreground (signal injections in [BBH, BNS]) and background (noise only) distributions from the following runs:
  - BBH template banks with and without injections, BNS template banks with and without injections.
  - Aggregate non-injection runs together as the background distribution, foreground will be one of [BBH, BNS] classes.
  - Remove contamination of background events from foreground events.

### Models

- Implement PyCBC Live MVP model. [add sources]
    - Integrate PyCBC's mass contour area calculations [COMPLETE]
    - Fit SPIIR's effective distance estimates to BAYESTAR luminosity distances. [IN PROGRESS]
- Implement FGMC model.
- Implement MC-FGMC model. (Optional)
- Evaluate model performance on injected simulated events.
- Evaluate model performance on known merger events (i.e. GWTC)


### Deployment

- Test IGWN-Alert on CIT systems.
  - https://git.ligo.org/lscsoft/igwn-alert/-/blob/main/share/igwn_alert_listener
- Test GitLab CI/CD integration with MLOps tools like DVC/CML.
  - Automate data extraction from a remote data repo with DVC.
  - Implement a training test and visualisation for git commits with CML.

