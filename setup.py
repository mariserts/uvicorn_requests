# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    # Application name:
    name="uvicorn_requests",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Maris Erts",
    author_email="maris@plain.ie",

    # Packages
    packages=["uvicorn_requests"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    license="LICENSE",
    description="#",

    # long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "Jinja2==3.1.2",
        "uvicorn==0.20.0",
    ],


)
