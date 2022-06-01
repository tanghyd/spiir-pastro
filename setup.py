from setuptools import setup, find_packages

setup(
    name="spiir-pastro",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="A Python application for SPIIR online p(astro)",
    author="Daniel Tang",
    author_email="daniel.tang@uwa.edu.au",
)