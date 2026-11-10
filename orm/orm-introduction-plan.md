# Presentation Plan: Introduction to ORMs

## Brief

- **Audience:** Beginner developers familiar with basic programming concepts.
- **Purpose:** Explain what an ORM is, how it connects objects to SQL tables, and when it is useful.
- **Language:** English.
- **Target duration:** About 5 minutes.
- **Assumptions:** A short introductory talk with no framework-specific prerequisites.

## Core message

An ORM lets developers work with relational data using objects in their programming language, but understanding SQL and databases remains important.

## Learning objectives

By the end, the audience will be able to:

1. Define the role of an ORM.
2. Explain the relationship between classes, objects, tables, and rows.
3. Give one benefit and one limitation of ORMs.

## Narrative

Start with the difference between the object-oriented world and relational tables, show how an ORM connects them, then illustrate the connection with a familiar query. Finish with productivity benefits and the importance of understanding what happens under the hood.

## Storyboard

| # | Title | Question / purpose | Main message | Example or visual |
|---|---|---|---|---|
| 1 | ORMs: From Objects to Tables | What is this talk about? | An ORM connects object-oriented code to a relational database. | Title and subtitle |
| 2 | Today’s Plan | What will the talk cover? | The talk moves from the problem to mapping, an example, trade-offs, and takeaways. | Five-item agenda |
| 3 | Two Worlds to Connect | Why do we need one? | Code works with objects; a relational database stores rows and columns. | Object / table comparison |
| 4 | Mapping in Practice | How are they connected? | Class → table, attribute → column, instance → row; relationships represent links between data. | Mapping diagram |
| 5 | One Request, Two Ways to Write It | What does the ORM do? | An ORM query expresses an intent that can also be written in SQL. | SQLAlchemy example and equivalent SQL query |
| 6 | Try It Yourself | Can I see it run? | A small SQLAlchemy script maps a Python class to an SQLite table and queries it. | Run `example/main.py` |
| 7 | Useful, but Not Magic | What are the trade-offs? | ORMs reduce repetitive code but do not eliminate SQL or performance concerns. | Benefits, caveats, and ORM examples |
| 8 | Key Takeaways | What should the audience remember? | An ORM is a convenience layer over the database, not a substitute for understanding it. | Summary and questions |
| 9 | Sources | Where can the audience learn more? | The examples and explanations are based on official documentation. | SQLAlchemy and Entity Framework Core links |

## Verified sources

- SQLAlchemy, “ORM Quick Start,” https://docs.sqlalchemy.org/en/20/orm/quickstart.html — accessed November 10, 2026.
- Microsoft, “Overview of Entity Framework Core,” https://learn.microsoft.com/en-us/ef/core/ — accessed November 10, 2026.

## Production notes

- **Visual direction:** Blue and white, large text, simple diagrams, following the provided Marp example.
- **Pacing:** About 35 to 45 seconds per slide.
- **Before presenting:** No statistics, prices, or comparative rankings are included; the live example is in `example/`.
