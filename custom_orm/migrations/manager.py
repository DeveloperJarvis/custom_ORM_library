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
# manager MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import importlib
import os
from typing import List

from custom_orm.database.connection import DatabaseConnection
from custom_orm.database.executor import SQLExecutor


# --------------------------------------------------
# migration manager
# --------------------------------------------------
class MigrationManager:
    """
    Handles database migrations.
    """

    MIGRATIONS_TABLE = "_migrations"

    def __init__(self, migrations_path: str):
        self.migrations_path = migrations_path
    
    # ----------------------
    # Public API
    # ----------------------
    def migrate(self):
        """
        Apply all pending migrations.
        """
        self._ensure_migrations_table()

        applied = self._get_applied_migrations()
        available = self._get_available_migrations()

        for migration in available:
            if migration not in applied:
                self._apply_migration(migration)
    
    # ----------------------
    # Internal helpers
    # ----------------------
    def _ensure_migrations_table(self):
        SQLExecutor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.MIGRATIONS_TABLE} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

    def _get_applied_migrations(self) -> List[str]:
        cursor = SQLExecutor.execute(
            f"SELECT name FROM {self.MIGRATIONS_TABLE}"
        )
        return [row["name"] for row in cursor.fetchall()]

    def _get_available_migrations(self) -> List[str]:
        files = []

        for filename in os.listdir(self.migrations_path):
            if (filename.endswith(".py")
                and filename != "__init__.py"):
                files.append(filename.replace(".py", ""))
        
        return sorted(files)

    def _apply_migration(self, migration_name: str):
        module = self._load_migration_module(
            migration_name)

        if not hasattr(module, "upgrade"):
            raise RuntimeError(
                f"Migration '{migration_name}' is "
                "missing upgrade()"
            )
        
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        try:
            module.upgrade(cursor)

            cursor.execute(
                f"""
                INSERT INTO {self.MIGRATIONS_TABLE} (name)
                VALUES (?)
                """,
                (migration_name,),
            )

            conn.commit()
        except Exception:
            conn.rollback()
            raise

    def _load_migration_module(self, name: str):
        """
        Dynamically import a migration module.
        """
        module_path = self._module_import_path(name)
        return importlib.import_module(module_path)

    def _module_import_path(self, name: str) -> str:
        """
        Convert filesystem path to Python import path.
        """
        base = self.migrations_path.replace(
            os.sep, ".").strip(".")
        return f"{base}.{name}"
