import sqlite3


def create_database():
    connection = sqlite3.connect("datahub.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_record(full_name, email, category, description):
    connection = sqlite3.connect("datahub.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO records (full_name, email, category, description)
        VALUES (?, ?, ?, ?)
    """, (full_name, email, category, description))

    connection.commit()
    connection.close()