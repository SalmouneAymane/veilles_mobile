---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: Arial, Helvetica, sans-serif;
    background: #ffffff;
    color: #172554;
    padding: 48px 64px;
    font-size: 1.3em;
  }
  section.title {
    background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 100%);
    color: #ffffff;
    text-align: center;
  }
  h1, h2 {
    color: #2563eb;
  }
  section.title h1,
  section.title h2 {
    color: #ffffff;
  }
  strong {
    color: #1d4ed8;
  }
  section.title strong {
    color: #bfdbfe;
  }
  code {
    background: #eff6ff;
    color: #be123c;
    font-size: 1em;
  }
  pre {
    background: #0f172a;
    color: #e2e8f0;
    border-radius: 8px;
    padding: 16px;
    font-size: 1em;
  }
---

<!-- _class: title -->
<!-- _paginate: false -->

# ORMs

### Connecting code objects to database tables

**Aymane Salmoune** |   **Fouad ESSARRAJ**

---

## Today’s plan

1. Why do we need ORMs?
2. How do objects map to tables?
3. ORM query vs. SQL
4. A runnable mini example
5. Benefits and trade-offs
6. Key takeaways

---

## Two worlds to connect

**In code:** objects, classes, and attributes  
**In a database:** tables, rows, and columns

Without an abstraction layer, developers have to connect these two representations themselves.

---

## How does an ORM work?

| In code | In a relational database |
|:---|:---|
| `User` class | `user` table |
| `name` attribute | `name` column |
| User object | Table row |
| Relationship between objects | Relationship between tables |

**ORM** stands for *Object-Relational Mapper*: a tool that maps objects to relational data.

---

## One request, two ways to write it

Example: find active users with SQLAlchemy.

```python
select(User).where(User.active.is_(True))
```

This SQLAlchemy statement expresses the intent; the ORM handles access to the database.

```sql
SELECT * FROM user WHERE active = TRUE;
```

*Simplified example: the table name and exact syntax depend on the model and database engine.*

---

## Try it yourself

The runnable example uses **SQLAlchemy** with an in-memory **SQLite** database.

```powershell
cd orm/example
python -m pip install -r requirements.txt
python main.py
```

See [`example/README.md`](example/README.md) for virtual environment setup and details.

---

## Useful, but not magic

**What an ORM offers**
- Less repetitive code for reading and changing data
- Work with results as objects in your programming language
- Abstraction over many data-access details

**What to keep in mind**
- Understanding SQL helps with debugging and optimization
- ORM queries can also be inefficient when used poorly
- An ORM does not replace good data modeling or transactions

**Examples:** Django ORM · SQLAlchemy · Hibernate · Entity Framework Core

---

<!-- _class: title -->
<!-- _paginate: false -->

# Key takeaways

An ORM bridges the **objects** in an application and the **tables** in a database.

It simplifies common tasks, but **SQL and database fundamentals still matter**.

### Questions?

---

## Sources

- SQLAlchemy — [ORM Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- Microsoft — [Overview of Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/)

*Documentation accessed November 10, 2026.*
