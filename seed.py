'''
The fucntion of the script is to create a database and seed it with initial data
if it does not already exist. In case the database already exists, it will return the
cursor to the SQLite Database.
'''
import sqlite3
import os


def seedDB():
    # Create connection
    connection = sqlite3.connect("bookmovies.db")

    # Create tables
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE movie (movieid INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute(
        "CREATE TABLE show (showid INTEGER PRIMARY KEY, movieid INTEGER, name TEXT, FOREIGN KEY(movieid) REFERENCES movie(movieid))")
    cursor.execute(
        "CREATE TABLE ticket (ticketid INTEGER PRIMARY KEY, showid INTEGER, username TEXT, seats INTEGER, FOREIGN KEY(showid) REFERENCES show(showid))")

    # Insert movies
    cursor.execute("INSERT INTO movie (name) VALUES ('Spider Man')")
    cursor.execute("INSERT INTO movie (name) VALUES ('Superman')")
    cursor.execute("INSERT INTO movie (name) VALUES ('Batman')")
    cursor.execute("INSERT INTO movie (name) VALUES ('Wonder Woman')")

    # Get the total number of movies
    total_movies = cursor.execute(
        "SELECT COUNT(*) FROM movie").fetchall()[0][0]

    # Insert shows
    for movie_id in range(1, total_movies + 1):
        for show_name in ['Morning', 'Matinee', 'Evening', 'Night']:
            cursor.execute(
                "INSERT INTO show (movieid, name) VALUES ('{}', '{}')".format(movie_id, show_name))

    # Return the cursor
    connection.commit()
    return connection


def getDB():
    # Check if the database exists
    if os.path.isfile('./bookmovies.db'):
        return sqlite3.connect("bookmovies.db")
    # Database does not exist
    return seedDB()


# print(os.path.isfile('./bookmovies.db'))
cur = getDB()
# data = cur.execute('select * from movie').fetchall()
# data = cur.execute('select * from show where movieid = 1').fetchall()
# print(data)
