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
# executor MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from custom_orm.database.connection import DatabaseConnection


# --------------------------------------------------
# SQL executor
# --------------------------------------------------
class SQLExecutor:
    @staticmethod
    def execute(sql: str, params=None):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        if DatabaseConnection._state.echo:
            print(sql, params)
        
        cursor.execute(sql, params or [])

        if not conn.in_transaction:
            conn.commit()
            
        return cursor
