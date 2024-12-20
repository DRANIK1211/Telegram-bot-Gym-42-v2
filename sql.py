import sqlite3 as sql

con = sql.connect("base.db")
cursor = con.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users ("
    "id INTEGER PRIMARY KEY,"
    "username TEXT NOT NULL,"
    "role TEXT NOT NULL,"
    "count INTEGER"  # User, Admin, IT, Xoz
    ")"
)


cursor.execute(
    "CREATE TABLE IF NOT EXISTS applications ("
    "id INTEGER PRIMARY KEY,"
    "sendersName TEXT NOT NULL,"
    "room TEXT NOT NULL,"
    "description TEXT NOT NULL,"
    "departament TEXT NOT NULL,"
    "date TEXT NOT NULL,"
    "status TEXT NOT NULL,"
    "performerName TEXT DEFAULT 'Not Started'"
    ")"
)


def search_user(id_user):
    user = cursor.execute("SELECT * FROM users WHERE id = ?", (id_user,)).fetchall()
    return user
    # Ищем в таблице users людей с id, в ответе массив [id, username, role, count]


def add_user(mas):  # Принимает массив параметров в формате [id, username, role, count]
    res = True
    try:  # Пробуем зарегистрировать пользователя. Если ошибок нет, возвращаем истину
        cursor.execute("INSERT INTO users (id, username, role, count) VALUES (?, ?, ?, ?)", mas)
        con.commit()
    except Exception as e:  # Если возникли ошибки, возвращаем для вывода
        res = f"Ошибка при добавлении пользователя: {e}"
    return res
    # Регистрация людей в бд


con.commit()
