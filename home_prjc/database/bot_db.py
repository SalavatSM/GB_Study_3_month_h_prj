import random
import sqlite3

db = sqlite3.connect("bot.sqlite3")
cursor = db.cursor()


def sql_create():
    # global db, cursor
    # db = sqlite3.connect("bot.sqlite3")
    # cursor = db.cursor()

    if db:
        print('Data Base connected!')

    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "mentor_id INTEGER UNIQUE, "
        "mentor_name VARCHAR (50), "
        "study_direction VARCHAR (70), "
        "mentor_age INTEGER, "
        "study_group TEXT)"
    )
    db.commit()


# sql_create()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(null, ?, ?, ?, ?, ?)", tuple(data.values())
                       )
        db.commit()


async def sql_command_random():
    users = cursor.execute("SELECT * FROM mentors").fetchall()
    random_users = random.choice(users)
    return random_users


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(mentor_id):
    cursor.execute("DELETE FROM mentors WHERE id == ?", (id,))
    db.commit()
