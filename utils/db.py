import sqlite3
import logging

def get_db():
    con = sqlite3.connect("mybot.db")
    cur = con.cursor()
    return con, cur



def create_user_table():
    con, cur = get_db()
    SQL = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER UNIQUE NOT NULL,
user_id VARCHAR(100) UNIQUE NOT NULL,
full_name VARCHAR(512),
username VARCHAR(255),
phone_number VARCHAR(20),
date_joined DATETIME default CURRENT_TIMESTAMP,
last_active DATETIME,

PRIMARY KEY(id AUTOINCREMENT)
)
"""
    cur.execute(SQL)
    con.commit()
    con.close()
    print("Users table created")
    return True


def create_or_update_user(user_id: str, full_name: str, username: str|None):
    from datetime import datetime
    now = datetime.now().strftime("%d-%m-%Y %H:%M")
    con, cur = get_db()

    SELECT_SQL = "SELECT id FROM users where user_id=?"
    cur.execute(SELECT_SQL, (user_id,))

    user = cur.fetchone()
    if user:
        UPDATE_SQL = """
UPDATE users SET full_name=?, username=?, last_active=? WHERE user_id=?
"""
        cur.execute(UPDATE_SQL, (full_name, username, now, user_id))
        con.commit()
        con.close()
        logging.info("User yangilandi")
        # print("User yangilandi", user_id)
        return False


    INSERT_SQL = """
INSERT INTO users(user_id, full_name, username, date_joined, last_active)
VALUES (?, ?, ?, ?, ?)
"""
    cur.execute(INSERT_SQL, (user_id, full_name, username, now, now))
    con.commit()
    con.close()
    logging.info("Yangi user qo'shildi")
    # print("Yangi user qo'shildi", user_id)
    return True


def create_messages_table():
    con, cur = get_db()
    SQL = """
CREATE TABLE IF NOT EXISTS messages(
id INTEGER NOT NULL UNIQUE,
user INTEGER NOT NULL,
message_id INTEGER,
message_text TEXT
created_at DATETIME,

PRIMARY KEY(id AUTOINCREMENT),
FOREIGN KEY(user) REFERENCES users(id)
)

"""

    cur.execute(SQL)
    con.commit()
    con.close()
    print("messages table created")
    return True


def record_message(user_id, message_id, message_text):
    from datetime import datetime
    now = datetime.now().strftime("%d-%m-%Y %H:%M")

    con, cur = get_db()

    GET_SQL = "SELECT id from users where user_id = ?"

    cur.execute(GET_SQL, [user_id])
    user = cur.fetchone()

    if not user:
        print("Xabar saqlanmadi. User topilmadi")
        return

    INSERT_SQL = """
INSERT INTO messages(user, message_id, message_text)
VALUES (?, ?, ?)
"""

    cur.execute(INSERT_SQL, [user[0], message_id, message_text])
    con.commit()
    con.close()
    print("Yangi xabar!")
    return True