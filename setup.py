# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Custom ORM Library Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Custom ORM Library - Map Python objects to SQLite tables
#               Skills: metaprogramming, SQL, abstraction design
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# setup MODULE
# --------------------------------------------------
"""
Purpose: packaging, installation, dependency declaration.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from setuptools import setup, find_packages


setup(
    name="custom-orm",
    version="0.1.0",
    description="A lightweight custom ORM mapping Python objects to SQLite",
    author="Developer Jarvis",
    author_email="developerjarvis@github.com",
    url="https://github.com/DeveloperJarvis/custom_ORM_library",
    license="GPL-3.0-or-later",
    packages=find_packages(
        exclude=("tests*", "logs*")
    ),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ]
    },
    classifiers=[
        "Programming Langauge :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
    ],
)
