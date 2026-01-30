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
# connection MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import sqlite3
from threading import local


# --------------------------------------------------
# database connection
# --------------------------------------------------
class DatabaseConnection:
    _state = local()

    @classmethod
    def initialize(cls, database: str, echo: bool = False):
        cls._state.database = database
        cls._state.echo = echo
        cls._state.connection = None
    
    @classmethod
    def get_connection(cls):
        if not hasattr(cls._state, "database"):
            raise RuntimeError(
                "DatabaseConnection.initialize() must "
                "be called first"
            )
        
        if getattr(cls._state, "connection", None) is None:
            cls._state.connection = sqlite3.connect(
                cls._state.database
            )
            cls._state.connection.row_factory = sqlite3.Row
        return cls._state.connection
    
    @classmethod
    def close(cls):
        conn = getattr(cls._state, "connection", None)
        if conn:
            conn.close()
            cls._state.connection = None
