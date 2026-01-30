@echo off

REM Root directory
@REM set ROOT=log_pattern_detection_tool
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\custom_orm"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\examples"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\custom_orm\database"
call :create_folder "%ROOT%\custom_orm\exceptions"
call :create_folder "%ROOT%\custom_orm\fields"
call :create_folder "%ROOT%\custom_orm\migrations"
call :create_folder "%ROOT%\custom_orm\models"
call :create_folder "%ROOT%\custom_orm\query"
call :create_folder "%ROOT%\custom_orm\schema"
call :create_folder "%ROOT%\custom_orm\utils"
call :create_folder "%ROOT%\custom_orm\validation"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\tests\integration"
call :create_folder "%ROOT%\tests\performance"
call :create_folder "%ROOT%\tests\regression"
call :create_folder "%ROOT%\tests\unit"
call :create_folder "%ROOT%\tests\unit\database"
call :create_folder "%ROOT%\tests\unit\fields"
call :create_folder "%ROOT%\tests\unit\queries"
call :create_folder "%ROOT%\tests\unit\schema"
call :create_folder "%ROOT%\tests\unit\validation"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\config\__init__.py"
call :create_py_file "%ROOT%\config\config.py"

call :create_py_file "%ROOT%\custom_orm\__init__.py"
call :create_py_file "%ROOT%\custom_orm\database\__init__.py"
call :create_py_file "%ROOT%\custom_orm\database\connection.py"
call :create_py_file "%ROOT%\custom_orm\database\executor.py"
call :create_py_file "%ROOT%\custom_orm\database\transaction.py"
call :create_py_file "%ROOT%\custom_orm\exceptions\__init__.py"
call :create_py_file "%ROOT%\custom_orm\exceptions\base.py"
call :create_py_file "%ROOT%\custom_orm\exceptions\database.py"
call :create_py_file "%ROOT%\custom_orm\exceptions\query.py"
call :create_py_file "%ROOT%\custom_orm\exceptions\schema.py"
call :create_py_file "%ROOT%\custom_orm\fields\__init__.py"
call :create_py_file "%ROOT%\custom_orm\fields\base.py"
call :create_py_file "%ROOT%\custom_orm\fields\relational.py"
call :create_py_file "%ROOT%\custom_orm\fields\scalar.py"
call :create_py_file "%ROOT%\custom_orm\migrations\__init__.py"
call :create_py_file "%ROOT%\custom_orm\migrations\manager.py"
call :create_py_file "%ROOT%\custom_orm\models\__init__.py"
call :create_py_file "%ROOT%\custom_orm\models\base.py"
call :create_py_file "%ROOT%\custom_orm\models\registry.py"
call :create_py_file "%ROOT%\custom_orm\query\__init__.py"
call :create_py_file "%ROOT%\custom_orm\query\compiler.py"
call :create_py_file "%ROOT%\custom_orm\query\expressions.py"
call :create_py_file "%ROOT%\custom_orm\query\query.py"
call :create_py_file "%ROOT%\custom_orm\schema\__init__.py"
call :create_py_file "%ROOT%\custom_orm\schema\generator.py"
call :create_py_file "%ROOT%\custom_orm\schema\inspector.py"
call :create_py_file "%ROOT%\custom_orm\schema\metadata.py"
call :create_py_file "%ROOT%\custom_orm\utils\__init__.py"
call :create_py_file "%ROOT%\custom_orm\utils\logging.py"
call :create_py_file "%ROOT%\custom_orm\utils\typing.py"
call :create_py_file "%ROOT%\custom_orm\validation\__init__.py"
call :create_py_file "%ROOT%\custom_orm\validation\fields.py"
call :create_py_file "%ROOT%\custom_orm\validation\models.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\conftest.py"
call :create_py_file "%ROOT%\tests\integration\__init__.py"
call :create_py_file "%ROOT%\tests\integration\test_constraints.py"
call :create_py_file "%ROOT%\tests\integration\test_crud.py"
call :create_py_file "%ROOT%\tests\integration\test_relationships.py"
call :create_py_file "%ROOT%\tests\integration\test_transactions.py"
call :create_py_file "%ROOT%\tests\performance\__init__.py"
call :create_py_file "%ROOT%\tests\performance\test_query_scaling.py"
call :create_py_file "%ROOT%\tests\regression\__init__.py"
call :create_py_file "%ROOT%\tests\regression\test_reported_bugs.py"
call :create_py_file "%ROOT%\tests\unit\__init__.py"
call :create_py_file "%ROOT%\tests\unit\database\__init__.py"
call :create_py_file "%ROOT%\tests\unit\database\test_connection.py"
call :create_py_file "%ROOT%\tests\unit\database\test_executor.py"
call :create_py_file "%ROOT%\tests\unit\database\test_transactions.py"
call :create_py_file "%ROOT%\tests\unit\fields\__init__.py"
call :create_py_file "%ROOT%\tests\unit\fields\test_base.py"
call :create_py_file "%ROOT%\tests\unit\fields\test_relations.py"
call :create_py_file "%ROOT%\tests\unit\fields\test_scalar.py"
call :create_py_file "%ROOT%\tests\unit\queries\__init__.py"
call :create_py_file "%ROOT%\tests\unit\queries\test_compiler.py"
call :create_py_file "%ROOT%\tests\unit\queries\test_expressions.py"
call :create_py_file "%ROOT%\tests\unit\queries\test_query.py"
call :create_py_file "%ROOT%\tests\unit\schema\__init__.py"
call :create_py_file "%ROOT%\tests\unit\schema\test_generator.py"
call :create_py_file "%ROOT%\tests\unit\schema\test_inspector.py"
call :create_py_file "%ROOT%\tests\unit\schema\test_metadata.py"
call :create_py_file "%ROOT%\tests\unit\validation\__init__.py"
call :create_py_file "%ROOT%\tests\unit\validation\test_fields.py"
call :create_py_file "%ROOT%\tests\unit\validation\test_models.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\logs\custom_orm.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Custom ORM Library Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Custom ORM Library - Map Python objects to SQLite tables
echo #               Skills: metaprogramming, SQL, abstraction design
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b