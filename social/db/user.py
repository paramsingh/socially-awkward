import sqlite3
from social.db import DATABASE_PATH
from flask_bcrypt import generate_password_hash


def create_user(username, password):
    pwd_hash = generate_password_hash(password)
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
    print(type(user_id), user_id)
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
            'passwd': row[2].decode('utf-8'),
        }
