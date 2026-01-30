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
# test_transactions MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from custom_orm.database.transaction import Transaction
from custom_orm.database.executor import SQLExecutor


def test_transaction_rollback():
    SQLExecutor.execute("CREATE TABLE test (id INTEGER)")
    
    with pytest.raises(Exception):
        with Transaction():
            SQLExecutor.execute(
                # "CREATE TABLE test (id INTEGER)"
                "INSERT INTO test (id) VALUES (1)"
            )
            raise RuntimeError("force rollback")
    
    cursor = SQLExecutor.execute(
        # "SELECT name FROM sqlite_master "
        # "WHERE type='table' AND name='test'"
        "SELECT * FROM test"
    )
    assert cursor.fetchone() is None
