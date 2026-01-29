## 📁 Examples Directory Structure

```
examples/
│
├── README.md
│
├── basics/
│   ├── define_model.md        # Declaring models & fields
│   ├── create_schema.md       # Table generation lifecycle
│   └── simple_crud.md         # Create, read, update, delete
│
├── queries/
│   ├── filtering.md           # WHERE, AND, OR conditions
│   ├── ordering_limit.md      # ORDER BY, LIMIT, OFFSET
│   └── lazy_evaluation.md     # Query building vs execution
│
├── relationships/
│   ├── foreign_key.md         # One-to-many relationships
│   ├── reverse_lookup.md      # Accessing related objects
│   └── lazy_loading.md        # Deferred relationship loading
│
├── validation/
│   ├── field_validation.md    # Type & constraint validation
│   └── model_validation.md    # Cross-field rules
│
├── transactions/
│   ├── atomic_operations.md   # Commit / rollback behavior
│   └── error_handling.md      # Failure recovery patterns
│
├── advanced/
│   ├── custom_fields.md       # Extending Field abstractions
│   ├── raw_sql.md             # Mixing ORM with raw SQL
│   └── performance_notes.md   # Avoiding N+1 queries
│
└── sqlite/
    ├── in_memory_db.md        # Testing & ephemeral databases
    └── file_based_db.md       # Persistent SQLite usage
```

---

## 📘 What Each Section Demonstrates

### 🔹 `basics/`

**Audience:** First-time users
**Purpose:** Establish mental model

- How a Python class becomes a table
- How instances map to rows
- What happens when `save()` is called
- When SQL is actually executed

---

### 🔹 `queries/`

**Audience:** Users coming from raw SQL
**Purpose:** Show abstraction without hiding SQL

- How filters translate to WHERE clauses
- How queries are composed step-by-step
- Why queries are lazy
- How to inspect generated SQL

---

### 🔹 `relationships/`

**Audience:** ORM users expecting relations
**Purpose:** Clarify limitations _and_ behavior

- Foreign key semantics
- When related objects are fetched
- Cost of relationship traversal
- How reverse lookups are implemented

---

### 🔹 `validation/`

**Audience:** Production-minded users
**Purpose:** Data correctness

- Field-level constraint enforcement
- Model-level invariants
- What fails early vs at DB level
- Error messages and exception types

---

### 🔹 `transactions/`

**Audience:** Backend / systems developers
**Purpose:** Data integrity

- Atomic operations
- Rollbacks on failure
- Nested transaction behavior (if supported)
- SQLite-specific caveats

---

### 🔹 `advanced/`

**Audience:** Power users / contributors
**Purpose:** Extensibility

- How to add a new Field type
- How to bypass ORM safely
- Performance trade-offs
- When _not_ to use the ORM

---

### 🔹 `sqlite/`

**Audience:** Practical users
**Purpose:** Environment clarity

- In-memory DB for tests
- File-based DB for apps
- Connection lifecycle
- SQLite-specific constraints

---

## 🧠 Design Philosophy Behind Examples

- **Narrative-first**: Each example tells a story
- **One concept per file**
- **No magic jumps**: every behavior is explained
- **Honest trade-offs**: limitations are documented

---

## 📌 Interview-Ready Summary

> “The examples are organized by learning progression: basics → queries → relationships → advanced usage. Each example explains not just _how_ the ORM works, but _why_ a design decision was made.”
