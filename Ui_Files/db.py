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

def AddNewBooking(movie, cinema, amount):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Booking VALUES(?,?,?)", (movie,cinema,amount))

    conn.commit()
    conn.close()

def AddNewGenre(genre):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Genre(genre) VALUES(?)", (genre,))

    conn.commit()
    conn.close()

def AddNewCinema(name, capacity):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Cinema(name, capacity) VALUES(?,?)", (name,capacity))

    conn.commit()
    conn.close()

def AddNewMovie(title, synopsis):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Movie(title, synopsis) VALUES(?,?)", (title,synopsis))

    conn.commit()
    conn.close()

def AddMovieGenre(movieID, genreID):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO MovieGenre(movieID, movieGenre) VALUES(?,?)", (movieID,genreID))

    conn.commit()
    conn.close()

def GetGenreList(cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT * FROM Genre {cond}").fetchall()
    conn.close()

    return res

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



