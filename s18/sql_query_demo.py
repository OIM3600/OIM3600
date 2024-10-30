import sqlite3


def query_countries(continent):
    """"""
    conn = sqlite3.connect("data/countries.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM countries WHERE continent=?", (continent,))
    results = cursor.fetchall()
    # print(results)

    for row in results:
        print(row[1])


def main():
    user_input = input("Continent > ")
    query_countries(user_input)


main()
