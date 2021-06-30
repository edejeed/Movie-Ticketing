import sqlite3

def Authenticate(user, password, priv=0):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM Users WHERE username = \'{user}\' AND password = \'{password}\' AND privilege = \'{priv}\'')
    rows = cur.fetchall()
    
    if len(rows) != 0:
        return True

    conn.close()

#ADD
def AddUser(user, password, priv = 0):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Users(username, password, privilege) VALUES(?,?,?)", (user,password, priv))

    conn.commit()
    conn.close()

def AddNewBooking(movie, cinema, amount):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Booking(movieID, cinemaID, noOfTickets) VALUES(?,?,?)", (movie,cinema,amount))

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

def AddNewShow(mID, cID, date, time, showing):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO MovieShowsAt(movieID, cinemaID, date, time, isShowing) VALUES(?,?,?,?,?)", (mID,cID, date, time, showing))

    conn.commit()
    conn.close()

#UPDATES
def UpdateGenre(id, genre):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE Genre SET genre = ? WHERE genreID = ?", (genre,id))

    conn.commit()
    conn.close()

def UpdateMovie(id, title, syn):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE Movie SET title = ?, synopsis = ? WHERE id = ?", (title,syn,id))

    conn.commit()
    conn.close()

def UpdateShow(id, mID, cID, date, time, showing):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE MovieShowsAt SET movieID = ?, cinemaID = ?, date = ?, time = ?, isShowing = ? WHERE showID = ?", (mID,cID, date, time, showing, id))

    conn.commit()
    conn.close()

def UpdateShowing(id):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE MovieShowsAt SET isShowing = ? WHERE showID = ?", (0,id))

    conn.commit()
    conn.close()

def UpdateCinema(id, name, capacity):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE Cinema SET name = ?, capacity = ? WHERE id = ?", (name, capacity,id))

    conn.commit()
    conn.close()

#GETS
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

def GetCinemaList(cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT * FROM Cinema {cond}").fetchall()
    conn.close()
    
    return res

def getScheduleList(movieID, cinemaID):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT date, time FROM MovieShowsAt WHERE movieID = {movieID} AND cinemaID = {cinemaID}").fetchall()

    conn.close()

    return res

def GetBookingList(cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT * FROM Booking {cond}").fetchall()

    conn.close()

    return res

def GetMovieCinemaOfBooking(cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT title, name, noOfTickets FROM Movie INNER JOIN Booking ON Movie.id = Booking.movieID INNER JOIN Cinema ON Booking.cinemaID = Cinema.id").fetchall()
    conn.close()

    return res

def GetShow(page, cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT title, synopsis, date, time, name, showID FROM Movie AS mov INNER JOIN MovieShowsAt AS show ON mov.id = show.movieID INNER JOIN Cinema AS cin ON show.cinemaID = cin.id WHERE show.isShowing = true LIMIT 6 OFFSET {(page-1)*6}").fetchall()
    conn.close()

    return res

def GetShowInfo(id, cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT * FROM MovieShowsAt WHERE showID = {id}").fetchall()
    conn.close()

    return res

def GetMovieGenre(cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"""
        SELECT * FROM 
            Movie AS mov INNER JOIN 
            MovieGenre AS mg ON mov.id = mg.movieID INNER JOIN
            Genre AS gen ON mg.movieGenre = gen.genreID
            {cond}
    """).fetchall()
    conn.close()

    return res

def GetUserList(priv, cond = ""):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()

    res = cur.execute(f"SELECT * FROM Users WHERE privilege = {priv} {cond}").fetchall()
    conn.close()

    return res

#Deletes
def DeleteGenre(id):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM Genre WHERE genreID = ?", (id,))

    conn.commit()
    conn.close()

def DeleteMovieGenre(id):
    conn = sqlite3.connect("MovieTicketingSystem.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM MovieGenre WHERE movieID = ?", (id,))

    conn.commit()
    conn.close()
    
