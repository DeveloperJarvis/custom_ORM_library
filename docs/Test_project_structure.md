## 🧪 Test Project Structure

```
tests/
│
├── __init__.py
│
├── conftest.py              # Shared fixtures (DB, temp files)
│
├── unit/
│   ├── __init__.py
│   │
│   ├── fields/
│   │   ├── test_base.py     # Field behavior & validation
│   │   ├── test_scalar.py  # Integer, Text, Boolean, etc.
│   │   └── test_relations.py
│   │
│   ├── schema/
│   │   ├── test_inspector.py   # Metaclass / class analysis
│   │   ├── test_metadata.py    # Schema metadata correctness
│   │   └── test_generator.py   # CREATE TABLE SQL generation
│   │
│   ├── queries/
│   │   ├── test_query.py       # Query object behavior
│   │   ├── test_expressions.py # WHERE / AND / OR logic
│   │   └── test_compiler.py    # SQL compilation accuracy
│   │
│   ├── database/
│   │   ├── test_connection.py  # Connection lifecycle
│   │   ├── test_executor.py    # SQL execution & mapping
│   │   └── test_transactions.py
│   │
│   └── validation/
│       ├── test_fields.py
│       └── test_models.py
│
├── integration/
│   ├── __init__.py
│   │
│   ├── test_crud.py            # Insert / Select / Update / Delete
│   ├── test_relationships.py   # ForeignKey behavior
│   ├── test_constraints.py     # UNIQUE / NOT NULL / FK
│   └── test_transactions.py
│
├── regression/
│   ├── __init__.py
│   └── test_reported_bugs.py   # Prevent bug reintroduction
│
└── performance/
    ├── __init__.py
    └── test_query_scaling.py   # Optional, non-blocking
```

---

## 🎯 Testing Strategy

### 1⃣ Unit Tests (Fast, Isolated)

**Goal:** Validate individual components _without_ a real database.

Test:

- Field validation logic
- Metaclass behavior (class → metadata)
- SQL generation correctness
- Query object immutability
- Error handling paths

**Why this matters**

- Catches logic bugs early
- Makes refactoring safe
- Keeps test runs fast

---

### 2⃣ Integration Tests (Real SQLite)

**Goal:** Ensure components work together correctly.

Test:

- Table creation
- Object persistence
- Dirty field updates
- Relationship resolution
- Transactions & rollbacks

**SQLite Mode**

- In-memory database (`:memory:`)
- Fresh schema per test

---

### 3⃣ Regression Tests

**Goal:** Lock in fixes permanently.

- Each bug gets its own test
- Named after the issue or behavior
- Prevents subtle ORM breakages

---

### 4⃣ Performance Tests (Optional but Impressive)

**Goal:** Detect ORM-level inefficiencies.

Test:

- N+1 query scenarios
- Bulk inserts
- Query compilation cost

These are usually:

- Marked as slow
- Excluded from CI by default

---

## 🔧 Fixtures Design (Conceptual)

### Common Fixtures

- Temporary SQLite database
- Test model definitions
- Schema setup & teardown
- Transaction rollback isolation

### Principles

- Tests never share DB state
- No order dependence
- Deterministic results

---

## 🔄 Typical Test Flow (Integration)

```
Setup SQLite (in-memory)
   ↓
Register models
   ↓
Generate schema
   ↓
Run ORM operation
   ↓
Assert DB + Object state
   ↓
Rollback / Teardown
```

---

## 📌 Interview-Ready Soundbite

> “Unit tests validate metaprogramming and SQL generation in isolation, while integration tests use an in-memory SQLite database to verify real object–row behavior. Regression tests protect against subtle ORM bugs.”
