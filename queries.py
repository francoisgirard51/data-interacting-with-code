""" This module contains all the queries used in the main.py file. """

def directors_count(database):
    """Return the number of directors contained in the database."""
    query = """
        SELECT COUNT(*)
        FROM directors
    """
    database.execute(query)
    count = database.fetchone()
    return count[0]

def directors_list(database):
    """Return the list of all the directors sorted in alphabetical order."""
    query = """
        SELECT name
        FROM directors
        ORDER BY name
    """
    database.execute(query)
    directors = database.fetchall()
    return [director[0] for director in directors]

def love_movies(database):
    """Return the list of all movies which contain the exact word 'love'
    in their title, sorted in alphabetical order."""
    query = """
        SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
    """
    database.execute(query)
    movies = database.fetchall()
    return [movie[0] for movie in movies]

def directors_named_like_count(database, name):
    """Return the number of directors which contain a given word in their name."""
    query = """
        SELECT COUNT(*)
        FROM directors
        WHERE name LIKE ?
    """
    database.execute(query, (f"%{name}%",))
    count = database.fetchone()
    return count[0]

def movies_longer_than(database, min_length):
    """Return the list of all movies which are longer than a given duration,
    sorted in alphabetical order."""
    query = """
        SELECT title
        FROM movies
        WHERE minutes > ?
        ORDER BY title
    """
    database.execute(query, (min_length,))
    movies = database.fetchall()
    return [movie[0] for movie in movies]
