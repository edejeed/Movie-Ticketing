import sqlite3


conn = sqlite3.connect("MovieTicketingSystem.db")
cur = conn.cursor()


def crew_password(user=None, password=None):
    cur.execute('SELECT * FROM Users WHERE username =?', (user,))
    rows = cur.fetchall()
    for row in rows:
        if user == row[1] and password == row[2]:
            return True





