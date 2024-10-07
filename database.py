import sqlite3


connection = sqlite3.connect('users.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS tg_users (tg_id INTEGER, name TEXT, tokens INTEGER);')


def register(tg_id, name, tokens=0):
    sql.execute('INSERT INTO tg_users VALUES (?, ?, ?);', (tg_id, name, tokens))
    connection.commit()


def add_token(tg_id):
    current_token = sql.execute('SELECT tokens FROM tg_users WHERE tg_id=?;', (tg_id,)).fetchone()[0]
    sql.execute('UPDATE tg_users SET tokens=? WHERE tg_id=?;', (current_token + 1, tg_id))
    connection.commit()


def check_user(tg_id):
    check = sql.execute('SELECT * FROM tg_users WHERE tg_id=?;', (tg_id,)).fetchone()
    if check:
        return True, check[2]
    else:
        return False
