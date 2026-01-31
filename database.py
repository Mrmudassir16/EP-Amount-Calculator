import sqlite3

DB_NAME = "ep_cases.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ep_cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suit_amount REAL,
            principal_amount REAL,
            suit_date TEXT,
            decree_date TEXT,
            ep_date TEXT,
            phase1_interest REAL,
            phase2_interest REAL,
            total_costs REAL,
            ep_amount REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_case(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ep_cases (
            suit_amount, principal_amount, suit_date,
            decree_date, ep_date,
            phase1_interest, phase2_interest,
            total_costs, ep_amount
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["suit_amount"],
        data["principal_amount"],
        data["suit_date"],
        data["decree_date"],
        data["ep_date"],
        data["phase1_interest"],
        data["phase2_interest"],
        data["total_costs"],
        data["ep_amount"]
    ))

    conn.commit()
    conn.close()
