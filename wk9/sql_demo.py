import sqlite3


# def query_countries():
#     """Make query in countries.db"""
#     conn = sqlite3.connect('data/countries.db')
#     cursor = conn.cursor()

#     continent = input('Continent: ')
#     cursor.execute("SELECT * FROM countries WHERE continent=?", (continent,))
#     results = cursor.fetchall()

#     cursor.close()
#     conn.close()

#     for row in results:
#         print(row)


# query_countries()


def query_shows():
    """Make query in shows.db, retrieve all the show by actor/actress"""
    # conn = sqlite3.connect('data/shows.db')
    # cursor = conn.cursor()

    # cursor.execute("SELECT Count(*) FROM shows")
    # results = cursor.fetchall()

    # cursor.close()
    # conn.close()

    name = input('Enter an actor/actress name: ')

    query = """SELECT shows.title, shows.year
            FROM shows JOIN stars ON shows.id = stars.show_id
            JOIN people ON stars.person_id = people.id
            WHERE name = ?;
            """

    with sqlite3.connect('data/shows.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, (name,))
        results = cursor.fetchall()

    for row in results:
        print(row)


query_shows()
