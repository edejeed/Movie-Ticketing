import sqlite3

def Authenticate(user, password, priv=0):
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

def AddBooking(movie, cinema, amount):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Booking VALUES(?,?,?)", (movie,cinema,amount))

    conn.commit()
    conn.close()

def AddGenre(genre):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Genre(genre) VALUES(?)", (genre,))

    conn.commit()
    conn.close()

def GetMovieList(cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT * FROM Movie {cond}").fetchall()
    conn.close()

    return res

def GetCinemaList():
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT * FROM Cinema").fetchall()
    conn.close()
    
    return res

def getScheduleList(movieID, cinemaID):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT date, time FROM MovieShowsAt WHERE movieID = {movieID} AND cinemaID = {cinemaID}").fetchall()

    conn.close()

    return res



