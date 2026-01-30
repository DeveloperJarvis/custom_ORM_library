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
# inspector MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from custom_orm.fields.base import Field
from custom_orm.schema.metadata import ModelMetadata


def inspect_model(model):
    fields = {}

    for name, attr in model.__dict__.items():
        if isinstance(attr, Field):
            attr.contribute_to_class(name)
            fields[name] = attr
    
    model._meta = ModelMetadata(
        table_name=model.__name__.lower(),
        fields=fields,
    )
