import sqlite3
from social.db import DATABASE_PATH
from flask_bcrypt import generate_password_hash

def _get_hash(text):
    return text

def create_user(username, password):
    pwd_hash = _get_hash(password)
    print("create: ", pwd_hash)
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO "user" (name, passwd)
                 VALUES (?, ?)
            """, (username, pwd_hash)
        )
        user_id = int(cursor.lastrowid)
    return get_user(user_id)


def get_user(user_id):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name, passwd
              FROM "user"
             WHERE id = ?;
        """, (user_id, ))
        row = cursor.fetchone()
        return {
            'id': row[0],
            'name': row[1],
        }


def get_by_username_and_password(user_name, password):
    pwd_hash = _get_hash(password)
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name, passwd
              FROM "user"
             WHERE name = ? AND passwd = ?
        """, (user_name, pwd_hash))
        row = cursor.fetchone()
        if row is None:
            return None, None
        return row[0], row[1]


def get_by_username(user_name):
    user_name = user_name.strip()
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, name, passwd
              FROM "user"
             WHERE name = ?
        """, (user_name,))
        row = cursor.fetchone()
        if row is None:
            return None, None
        return row[0], row[1]
