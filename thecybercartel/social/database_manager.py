import sqlite3


conn = sqlite3.connect("thecybercartel.db")


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
    cursor = conn.cursor()
    for stm in stms:
        cursor.execute(stm)
    conn.commit()
