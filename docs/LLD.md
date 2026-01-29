# **LLD (Low-Level Design)** for a **custom Python ORM that maps Python objects to SQLite tables**

---

## 1. Design Goals

**Primary goals**

- Map Python classes → SQLite tables
- Map Python objects → table rows
- Provide CRUD operations with minimal SQL exposure
- Support relationships (basic)
- Be lightweight and explicit (not a Django clone)

**Non-goals**

- No distributed DB support
- No advanced query planner
- No migration engine (optional extension)

---

## 2. High-Level Architecture

```
User Model Class
   ↓
Metaclass / Class Analyzer
   ↓
Schema Metadata Registry
   ↓
Query Builder → SQL Generator
   ↓
SQLite Adapter
   ↓
sqlite3 connection
```

---

## 3. Core Components

### 3.1 Field Abstractions (Column Mapping)

Each table column is represented by a **Field descriptor abstraction**.

**Responsibilities**

- Hold column metadata:
  - name
  - SQLite type (INTEGER, TEXT, REAL, BLOB)
  - constraints (PRIMARY KEY, UNIQUE, NOT NULL, DEFAULT)

- Validate values before persistence
- Control attribute access on instances

**Design Notes**

- Uses Python **descriptor protocol** conceptually
- When accessed on:
  - Class → returns column metadata
  - Instance → returns stored value

---

### 3.2 Model Base Class

All ORM models inherit from a common `Model` abstraction.

**Responsibilities**

- Provide CRUD APIs:
  - save()
  - delete()
  - get()
  - filter()

- Hold instance state:
  - dirty fields
  - primary key value

- Bridge object ↔ row conversion

**Internal State**

- `_data`: current field values
- `_original_data`: snapshot for change tracking
- `_meta`: schema metadata reference

---

### 3.3 Metaclass / Class Processing Layer

This is the **heart of metaprogramming**.

**Triggered when a Model subclass is defined**

**Responsibilities**

- Scan class attributes
- Identify Field instances
- Remove them from class namespace
- Build schema metadata:
  - table name
  - column definitions
  - primary key

- Register model in a global registry

**Why a Metaclass**

- Runs **once at class creation**
- Enables automatic schema generation
- Avoids runtime reflection overhead

---

### 3.4 Schema Metadata Registry

A centralized structure storing model definitions.

**Per Model Metadata**

- Table name
- Columns
- Column → Field mapping
- Primary key
- Indexes (optional)

**Global Registry**

- Maps model name → metadata
- Used by:
  - Query builder
  - Migration tools
  - Table creation logic

---

## 4. SQLite Adapter Layer

### 4.1 Connection Manager

**Responsibilities**

- Manage SQLite connection lifecycle
- Provide thread-safe access (if needed)
- Handle transactions:
  - begin
  - commit
  - rollback

**Design Choice**

- Single connection per thread
- Lazy initialization

---

### 4.2 SQL Executor

**Responsibilities**

- Execute generated SQL
- Bind parameters safely
- Convert SQLite rows → Python primitives
- Handle SQLite-specific behavior:
  - AUTOINCREMENT
  - last_insert_rowid()

---

## 5. Query System Design

### 5.1 Query Object

Instead of executing immediately, queries are **built incrementally**.

**Responsibilities**

- Store query intent:
  - SELECT / INSERT / UPDATE / DELETE
  - filters
  - ordering
  - limits

- Lazily evaluated

**Benefits**

- Chainable API
- SQL generation happens once
- Easier debugging and logging

---

### 5.2 SQL Generator

Converts Query objects → SQLite SQL strings.

**Responsibilities**

- Map fields → column names
- Generate:
  - WHERE clauses
  - parameter placeholders

- Respect SQLite syntax
- Prevent SQL injection via parameterization

---

## 6. Object ↔ Row Mapping Flow

### 6.1 Insert Flow

1. User creates model instance
2. Fields store values via descriptors
3. save() called
4. ORM detects no primary key
5. INSERT SQL generated
6. SQLite assigns rowid
7. ORM updates instance primary key
8. Object marked clean

---

### 6.2 Fetch Flow

1. Query executed
2. SQLite returns rows
3. ORM:
   - creates empty model instances
   - populates `_data`
   - skips `__init__`

4. Objects returned to user

---

### 6.3 Update Flow

1. Field modified
2. Dirty tracking marks field
3. save() called
4. UPDATE SQL generated for dirty fields only
5. WHERE primary_key = ?

---

## 7. Relationship Design (Minimal)

### 7.1 Foreign Key Field

**Concept**

- Stores referenced model + column
- Value stored as foreign key ID
- Lazy-load related object

**Example Behavior (conceptual)**

- `post.author` triggers SELECT on User table
- Cached after first load

---

### 7.2 One-to-Many

- Implemented via reverse query:
  - `user.posts` → filter(Post.author_id == user.id)

---

## 8. Validation & Constraints

**Field-level validation**

- Type checks
- Nullability
- Length constraints

**Model-level validation**

- Hook before save
- Cross-field rules

---

## 9. Error Handling Strategy

**Error Types**

- Schema errors (missing PK, duplicate fields)
- Validation errors
- SQLite constraint violations

**Approach**

- Wrap SQLite errors
- Re-raise as ORM-specific exceptions
- Preserve original error message

---

## 10. Extensibility Points

- Custom Field types
- Query optimizers
- Migrations
- Caching layer
- Async adapter (aiosqlite)

---

## 11. Design Trade-offs

**Pros**

- Lightweight
- Transparent SQL
- Strong Python introspection usage

**Cons**

- No advanced query planner
- Limited relationship handling
- Manual migrations
