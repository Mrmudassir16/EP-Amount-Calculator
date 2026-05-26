import sqlite3


DB_NAME = "ep_cases.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # If database layout is old (fewer columns), drop it to recreate it safely
    try:
        cursor.execute("PRAGMA table_info(ep_cases)")
        columns = cursor.fetchall()
        if columns and len(columns) < 16:
            cursor.execute("DROP TABLE ep_cases")
    except sqlite3.OperationalError:
        pass

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ep_cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suit_amount REAL,
            principal_amount REAL,
            suit_date TEXT,
            decree_date TEXT,
            ep_date TEXT,
            rate_suit_decree REAL,
            rate_decree_ep REAL,
            costs_awarded REAL,
            cost_obtaining REAL,
            court_fee_ep REAL,
            court_fee_decree REAL,
            advocate_fee_ep REAL,
            suit_contested TEXT,
            final_amount REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_case(
    suit_amount,
    principal_amount,
    suit_date,
    decree_date,
    ep_date,
    rate_suit_decree,
    rate_decree_ep,
    costs_awarded,
    cost_obtaining,
    court_fee_ep,
    court_fee_decree,
    advocate_fee_ep,
    suit_contested,
    final_amount
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ep_cases (
            suit_amount,
            principal_amount,
            suit_date,
            decree_date,
            ep_date,
            rate_suit_decree,
            rate_decree_ep,
            costs_awarded,
            cost_obtaining,
            court_fee_ep,
            court_fee_decree,
            advocate_fee_ep,
            suit_contested,
            final_amount
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        suit_amount,
        principal_amount,
        suit_date,
        decree_date,
        ep_date,
        rate_suit_decree,
        rate_decree_ep,
        costs_awarded,
        cost_obtaining,
        court_fee_ep,
        court_fee_decree,
        advocate_fee_ep,
        suit_contested,
        final_amount
    ))

    conn.commit()
    conn.close()


def get_all_cases():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ep_cases ORDER BY id DESC")
    rows = cursor.fetchall()
    cases = [dict(row) for row in rows]
    conn.close()
    return cases


def delete_case(case_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ep_cases WHERE id = ?", (case_id,))
    conn.commit()
    conn.close()

