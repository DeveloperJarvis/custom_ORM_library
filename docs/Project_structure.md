## 📁 Project Structure

```
custom_orm/
│
├── __init__.py
│
├── models/
│   ├── __init__.py
│   ├── base.py              # Base Model abstraction
│   └── registry.py          # Global model registry
│
├── fields/
│   ├── __init__.py
│   ├── base.py              # Field descriptor abstraction
│   ├── scalar.py            # Integer, Text, Float, Boolean fields
│   └── relational.py        # ForeignKey and relationship fields
│
├── schema/
│   ├── __init__.py
│   ├── metadata.py          # Table & column metadata objects
│   ├── inspector.py         # Model class analyzer (metaprogramming)
│   └── generator.py         # CREATE TABLE SQL generation
│
├── queries/
│   ├── __init__.py
│   ├── query.py             # Query object (lazy evaluation)
│   ├── expressions.py       # WHERE, AND, OR expressions
│   └── compiler.py          # Query → SQLite SQL compiler
│
├── database/
│   ├── __init__.py
│   ├── connection.py        # SQLite connection manager
│   ├── transaction.py       # Transaction handling
│   └── executor.py          # SQL execution & result mapping
│
├── validation/
│   ├── __init__.py
│   ├── fields.py            # Field-level validation
│   └── models.py            # Model-level validation hooks
│
├── exceptions/
│   ├── __init__.py
│   ├── base.py              # Base ORM exception
│   ├── schema.py            # Schema & mapping errors
│   ├── query.py             # Query construction errors
│   └── database.py          # SQLite execution errors
│
├── utils/
│   ├── __init__.py
│   ├── typing.py            # Shared typing helpers
│   └── logging.py           # Debug & SQL logging
│
├── migrations/              # (Optional / future)
│   ├── __init__.py
│   └── manager.py
│
└── README.md
```

---

## 🧠 Design Rationale (Why This Structure Works)

### 🔹 Separation of Concerns

Each layer owns exactly one responsibility:

- **models** → object lifecycle & behavior
- **fields** → column definitions & descriptors
- **schema** → class analysis & table definitions
- **queries** → query intent & SQL generation
- **database** → execution & SQLite interaction

---

### 🔹 Metaprogramming Isolation

All class inspection and magic lives in:

```
schema/inspector.py
```

This keeps metaclasses and reflection **out of business logic**, making the system easier to reason about.

---

### 🔹 Database Agnostic (Future-Proof)

Although SQLite-focused, DB-specific logic is isolated in:

```
database/
queries/compiler.py
```

Allowing future adapters (Postgres, MySQL) without touching models.

---

### 🔹 Extensibility Without Refactoring

You can add:

- New field types → `fields/`
- Query operators → `queries/expressions.py`
- Async support → `database/`
- Migrations → `migrations/`

…without breaking existing APIs.

---

## 🔄 Typical Flow Across Modules

```
Model Class
   ↓ (schema.inspector)
Schema Metadata
   ↓
Query Object
   ↓ (queries.compiler)
SQL String
   ↓
database.executor
   ↓
SQLite
```

---

## 📌 Interview-Friendly Summary

> “The project is organized by responsibility rather than features.
> Metaprogramming is isolated to schema inspection, SQL generation is decoupled from execution, and the model layer remains clean and expressive.”
