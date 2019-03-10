import os
import sqlite3

DATABASE_PATH = os.path.join('..', os.path.dirname(os.path.realpath(__file__)), 'socialize.sqlite3')

def drop_tables():
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.executemany("""
            DROP TABLE IF EXISTS user;
            DROP TABLE IF EXISTS post;
            DROP TABLE IF EXISTS follow;
        """)


def create_tables():
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS "user" (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT NOT NULL UNIQUE,
                passwd  TEXT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS post (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                message TEXT NOT NULL,
                created DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES "user"(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS follow (
                follower  INTEGER,
                following TEXT NOT NULL,
                FOREIGN KEY (follower) REFERENCES "user"(id)
            );
        """)

