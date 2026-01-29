# Custom ORM Library

**Custom ORM Library** is a lightweight Object–Relational Mapping (ORM) framework designed to map Python objects to SQLite database tables.
The project emphasizes **metaprogramming**, **SQL abstraction**, and **clean architectural design**, making it suitable both as a learning reference and as a foundation for small to medium applications.

---

## ✨ Features

- Python class → SQLite table mapping
- Object instance → table row persistence
- Automatic schema introspection via metaprogramming
- Clean separation between:
  - Models
  - Schema metadata
  - Query generation
  - Database execution

- Minimal, explicit SQL abstraction (no magic-heavy behavior)
- SQLite-focused for simplicity and portability

---

## 🎯 Design Goals

- **Simplicity** – Easy to understand and extend
- **Transparency** – Generated SQL remains predictable
- **Lightweight** – No external ORM dependencies
- **Educational Value** – Clear demonstration of ORM internals

---

## 🚫 Non-Goals

- No support for non-SQLite databases
- No automatic migration engine
- No distributed or asynchronous query execution
- Not intended to replace full-featured ORMs like Django ORM or SQLAlchemy

---

## 🧠 Core Concepts

### 1. Models

- Python classes represent database tables
- Instances represent rows
- Fields define columns and constraints

### 2. Metaprogramming

- Model classes are analyzed at definition time
- Field metadata is extracted and registered
- Schema information is built automatically

### 3. Schema Metadata Registry

- Centralized storage of:
  - Table names
  - Columns
  - Primary keys
  - Constraints

- Used by query builders and SQL generators

### 4. Query Abstraction

- Queries are constructed as objects
- SQL is generated lazily
- Parameterized execution prevents SQL injection

### 5. SQLite Adapter

- Handles connections and transactions
- Executes generated SQL
- Maps query results back to Python objects

---

## 🔄 Object Lifecycle

1. **Define Model**
   Python class is analyzed and registered.

2. **Create Instance**
   Field values are stored and tracked.

3. **Persist**
   Object state is translated into SQL (`INSERT` / `UPDATE`).

4. **Query**
   Database rows are converted back into model instances.

---

## 🔗 Relationships (Basic)

- Foreign key fields reference other models
- Related objects can be lazily loaded
- One-to-many relationships are supported via reverse lookups

---

## 🧪 Validation & Error Handling

- Field-level validation (type, nullability)
- Model-level validation hooks
- SQLite errors wrapped in ORM-specific exceptions
- Clear distinction between schema errors and runtime errors

---

## 🧩 Extensibility

The library is designed to be extended with:

- Custom field types
- Query optimizations
- Migration tooling
- Caching layers
- Async database adapters

---

## 📁 Project Structure (Conceptual)

```
custom_orm/
├── models/
├── fields/
├── schema/
├── queries/
├── database/
└── exceptions/
```

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0 or later**.

See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) file for details.

---

## 👤 Author

**Developer Jarvis** (Pen Name)
GitHub: [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)

---

## 📌 Status

This project is under active development and is intended for:

- Educational purposes
- Design exploration
- Lightweight SQLite-backed applications
