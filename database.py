import sqlite3


DB_NAME = "ep_cases.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ep_cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suit_amount REAL,
            principal_amount REAL,
            final_amount REAL
        )
    """)

    conn.commit()
    conn.close()


def save_case(suit_amount, principal_amount, final_amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ep_cases (suit_amount, principal_amount, final_amount)
        VALUES (?, ?, ?)
    """, (suit_amount, principal_amount, final_amount))

    conn.commit()
    conn.close()
