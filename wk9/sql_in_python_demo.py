import sqlite3


def query_countries():
    """
    Make query in countries.db
    """
    conn = sqlite3.connect("data/countries.db")
    cursor = conn.cursor()
    continent = input("Continent: ")
    # Excute SQL query
    cursor.execute("SELECT * FROM countries WHERE continent=?", (continent,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in results:
        print(row)


# query_countries()


def query_shows():
    """Print all the shows from shows.db"""
    # conn = sqlite3.connect("data/shows.db")
    # cursor = conn.cursor()
    # # Excute SQL query
    # cursor.execute("SELECT * FROM shows")
    # results = cursor.fetchall()
    # cursor.close()
    # conn.close()

    # Using Python's context manager
    with sqlite3.connect("data/shows.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM shows")
        results = cursor.fetchall()

    for row in results:
        print(row)


# query_shows()


def query_shows_2():
    """
    Ask user to enter an actor/actress name, and print all the shows they were in.
    """
    name = input("Enter an actor/actress name: ")

    query = """
    SELECT title
    FROM people JOIN stars
    ON people.id = stars.person_id
    JOIN shows
    ON stars.show_id = shows.id
    WHERE name = ?;
    """

    with sqlite3.connect("data/shows.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, (name,))
        results = cursor.fetchall()

    for row in results:
        print(*row)


query_shows_2()
