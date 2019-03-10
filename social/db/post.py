import sqlite3
from social.db import DATABASE_PATH
from flask_bcrypt import generate_password_hash

def create_post(user_id, post):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO "post" (user_id, message)
                 VALUES (?, ?)
            """, (user_id, post)
        )
        user_id = int(cursor.lastrowid)
    #return get_post(user_id)
    return "Posted Successfully"


def get_posts(user_id):
    print(type(user_id), user_id)
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT user_id, message
              FROM "post"
             WHERE id = ?;
        """, (user_id, ))
        rows = cursor.fetchall()
        return [{
            'user_id': row[0],
            'post': row[1].decode('utf-8'),
        } for row in rows]
