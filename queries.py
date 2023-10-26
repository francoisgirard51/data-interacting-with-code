""" This module contains the queries to be implemented.
"""

import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

def directors_count(db):
    """Return the number of directors contained in the database.
    """
    query = "SELECT COUNT(*) FROM directors"
    db.execute(query)
    count = db.fetchone()[0]
    return count

def directors_list(db):
    """return the list of all the directors sorted in alphabetical order
    """
    query = "SELECT name FROM directors ORDER BY name"
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]

def love_movies(db):
    """return the list of all movies which contain the exact word "love"
    in their title, sorted in alphabetical order
    """
    query = """
    SELECT title FROM movies
    WHERE title LIKE ?
        OR title LIKE ?
        OR title LIKE ?
        OR title LIKE ?
        OR title LIKE ?
        OR title LIKE ?
        OR title LIKE ?
    ORDER BY title
    """
    db.execute(query, (
        '% love %', #
        '% love', #
        'love %', #
        '%love,%', #
        '% love.%', #
        "% love'%", #
        'love'
    ))
    results = db.fetchall()
    return [row[0] for row in results]

def directors_named_like_count(db, name):
    """return the number of directors which contain a given word in their name
    """
    query = "SELECT COUNT(*) FROM directors WHERE name LIKE ?"
    db.execute(query, ('%' + name + '%',))
    count = db.fetchone()[0]
    return count

def movies_longer_than(db, min_length):
    """return this list of all movies which are longer than a given duration,
    sorted in the alphabetical order
    """
    query = "SELECT title FROM movies WHERE minutes > ? ORDER BY title"
    db.execute(query, (min_length,))
    results = db.fetchall()
    return [row[0] for row in results]

if __name__ == "__main":
    print("Number of Directors:", directors_count(db))
    print("Directors List:")
    for director in directors_list(db):
        print(director)
    print("Movies with 'love' in title:")
    for movie in love_movies(db):
        print(movie)
    print("Directors with 'Steven' in their name:", directors_named_like_count(db, 'Steven'))
    print("Movies longer than 120 minutes:")
    for movie in movies_longer_than(db, 120):
        print(movie)

conn.close()
