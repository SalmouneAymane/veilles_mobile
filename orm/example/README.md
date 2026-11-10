# Runnable ORM example

This mini example uses SQLAlchemy 2.x and SQLite to show how a Python `User` class maps to a database table. It creates an in-memory database, adds two users, and queries for active users. The database is recreated each time the program runs.

## Requirements

- Python 3.10 or later
- Internet access for the initial SQLAlchemy installation

## Run on Windows (PowerShell)

From the project root:

```powershell
cd orm\example
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

If PowerShell blocks activation, run the script with the virtual environment's interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## Run on macOS or Linux

From the project root:

```bash
cd orm/example
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Expected output

```text
Active users:
- Aymane (id: 1)
```

The ORM query is:

```python
select(User).where(User.active.is_(True)).order_by(User.name)
```

Its SQL equivalent is conceptually:

```sql
SELECT users.id, users.name, users.active
FROM users
WHERE users.active IS TRUE
ORDER BY users.name
```
