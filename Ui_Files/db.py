import sqlite3


conn = sqlite3.connect("MovieTicketingSystem.db")
cur = conn.cursor()


def crew_login(user=None, password=None):
    cur.execute('SELECT * FROM "Users"')
    rows = cur.fetchall()

    for row in rows:
        if user == row[0] and password == row[1]:
            return True
        return False


