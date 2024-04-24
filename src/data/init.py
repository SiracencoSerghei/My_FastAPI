import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None = None
curs: Cursor | None = None

def get_db(name: str|None = None, reset: bool = False):
    """Connect to SQLite database file"""
    global conn, curs
    if conn:
        if not reset:
            return
        conn = None
    if not name:
        top_dir = Path(__file__).resolve().parent.parent
        print(f"{top_dir=}")
        db_dir = top_dir / "db"
        db_name = "cryptid.db"
        db_path = db_dir / db_name
        if not db_dir.exists():
            db_dir.mkdir(parents=True)  # Create the db directory if it doesn't exist
        name = str(db_dir / db_name)
    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()

get_db()
