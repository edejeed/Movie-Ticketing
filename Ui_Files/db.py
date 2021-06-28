import sqlite3

def Authenticate(user=None, password=None, priv=0):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM Users WHERE username = \'{user}\' AND password = \'{password}\' AND privilege = \'{priv}\'')
    rows = cur.fetchall()
    
    if len(rows) != 0:
        return True
        
    # for row in rows:
    #     if user == row[1] and password == row[2]:
    #         return True

    conn.close()



