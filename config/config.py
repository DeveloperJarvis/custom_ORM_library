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
# config MODULE
# --------------------------------------------------
"""
Purpose: centralized configuration (simple, explicit,
test-friendly).
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from dataclasses import dataclass


# --------------------------------------------------
# settings
# --------------------------------------------------
@dataclass(frozen=True)
class Settings:
    """
    Application configuration.
    """

    # Database
    DATABASE_PATH: str = os.getenv("CUSTOM_ORM_DB",
                                   "custome_orm.db")
    
    # Debug / logging
    SQL_ECHO: bool = os.getenv("CUSTOM_ORM_SQL_ECHO",
                               "false").lower() == "true"
    BASE_DIR = os.path.join(os.path.abspath(__file__),
                            "..")
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    LOG_FILE = os.path.join(LOG_DIR, "custom_orm.log")

    LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    
    # Environment
    ENV: str = os.getenv("CUSTOM_ORM_ENV", "development")


settings = Settings()
