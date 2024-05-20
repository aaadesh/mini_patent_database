import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'patents_database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
