#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

from geoscience import __version__

REPO_URL = "https://github.com/SSJenny90/django-earth-science"

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-earth-science",
    packages=find_packages(),
    include_package_data=True,
    version=__version__,
    author="Sam Jennings",
    author_email="samuel.jennings@geoluminate.com.au",
    license="MIT",
    description="Django fields and utilites for the Earth Sciences",
    url=REPO_URL,
    install_requires=[
        "Django>=3",
        "django-treebeard",
        "django-treewidget",
    ],
    keywords="science django geology geoscience earth earthscience",
    classifiers=[
        "Development Status :: 1 - Development",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
