import os
import sqlite3

DATABASE_PATH = os.path.join('..', os.path.dirname(os.path.realpath(__file__)), 'socialize.db')


def create_tables():
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE "user" (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                name       TEXT NOT NULL,
                passcode   TEXT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE post (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                message TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES "user"(id)
            );
        """)

