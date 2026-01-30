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
# test_crud MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from custom_orm.models.base import Model
from custom_orm.fields.scalar import (
    IntegerField,
    TextField
)
from custom_orm.schema.generator import SchemaGenerator
from custom_orm.database.executor import SQLExecutor


# --------------------------------------------------
# user
# --------------------------------------------------
class User(Model):
    id = IntegerField(primary_key=True)
    name = TextField()


def test_insert_and_select():
    SchemaGenerator.generate(User)

    SQLExecutor.execute(
        "INSERT INTO user (id, name) VALUES (?, ?)",
        [1, "Alice"]
    )

    cursor = SQLExecutor.execute(
        "SELECT name FROM user WHERE id = ?", [1]
    )
    row = cursor.fetchone()

    assert row["name"] == "Alice"
