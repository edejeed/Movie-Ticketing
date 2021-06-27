tables = [
'''CREATE TABLE IF NOT EXISTS Movie(
	id 		INT SERIAL,
	title	 	VARCHAR(50) NOT NULL,
	synopsis		TEXT NOT NULL,
	PRIMARY KEY(id)
); ''',
'''CREATE TABLE IF NOT EXISTS Genre(
	genreID		INT SERIAL,
	genre		VARCHAR(50) NOT NULL,
	PRIMARY KEY(genreID)
);''',
'''CREATE TABLE IF NOT EXISTS MovieGenre(
	movieID		INT NOT NULL,
	movieGenre	INT NOT NULL,
	FOREIGN KEY(movieID) REFERENCES Movie(id),
	FOREIGN KEY(movieGenre) REFERENCES Genre(genreID)
);''',
'''CREATE TABLE IF NOT EXISTS Cinema(
	id		INT SERIAL,
	name		VARCHAR(15) NOT NULL,
	capacity		INT NOT NULL,
	PRIMARY KEY(id)
);''',
'''CREATE TABLE IF NOT EXISTS MovieShowsAt(
	movieID		INT NOT NULL,
	cinemaID	INT NOT NULL,
	date		DATE NOT NULL,
	time 		TIME NOT NULL,
	isShowing	BOOLEAN NOT NULL,
	FOREIGN KEY(movieID) REFERENCES Movie(id),
	FOREIGN KEY(cinemaID) REFERENCES Cinema(id)
);''',
'''CREATE TABLE IF NOT EXISTS Booking(
	movieID		INT NOT NULL,
	cinemaID	INT NOT NULL,
	noOfTickets	INT NOT NULL,
FOREIGN KEY(movieID) REFERENCES Movie(id),
	FOREIGN KEY(cinemaID) REFERENCES Cinema(id)
);''',
'''CREATE TABLE IF NOT EXISTS Users(
	id		INT SERIAL,
	username	VARCHAR(50) NOT NULL,
	password	VARCHAR(50) NOT NULL,
	privilege		INT NOT NULL,
	PRIMARY KEY(id)
);'''

]