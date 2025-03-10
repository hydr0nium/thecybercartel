import sqlite3
import hashlib
import secrets


def init():
    stms = ['''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    creator INTEGER NOT NULL,
    content text NOT NULL,
    likes INTEGER NOT NULL,
    timestamp INTEGER NOT NULL
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    commenter INTEGER NOT NULL,
    content text NOT NULL,
    likes INTEGER NOT NULL,
    timestamp INTEGER NOT NULL
    );
    '''
    ]
    conn = sqlite3.connect("thecybercartel.db")
    cursor = conn.cursor()
    for stm in stms:
        cursor.execute(stm)
    conn.commit()


def create_user(username, password):
    conn = sqlite3.connect("thecybercartel.db")
    stmt = "SELECT * FROM users WHERE username = (?)"
    cursor = conn.cursor()
    cursor.execute(stmt, (username,))
    result = cursor.fetchall()
    print(result)
    
    stmt = "SELECT COUNT(*) FROM users WHERE username = (?)"
    cursor = conn.cursor()
    cursor.execute(stmt, (username,))
    result = cursor.fetchone()
    row_count = result[0]
    print(row_count)
    if row_count != 0:
        return False

    salt = secrets.token_hex(8)
    hash = hashlib.sha256(bytes(salt + password, "utf-8"))
    hashed_password = salt + "." + hash.hexdigest()
    stmt = "INSERT INTO users (username, password) VALUES (?,?)"
    cursor = conn.cursor()
    cursor.execute(stmt, (username, hashed_password))
    conn.commit()
    return True