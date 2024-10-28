# SQL Commands Summary and Instructions

This guide provides a step-by-step walkthrough of SQL commands using SQLite, covering examples with country data and IMDB data. It includes instructions on how to create databases, import data, perform queries, and optimize performance using indexes.

## Countries Database Example (countries.db)

### 1. Start SQLite3

Open the SQLite3 command-line interface in VSCode Terminal:

```shell
> cd data
> sqlite3

SQLite version 3.46.1 2024-08-13 09:16:08 (UTF-16 console I/O)
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
```
To exit the SQLite3 command-line interface, type `.quit`:
```shell
sqlite3> .quit
```

### 2. Create a Database and Import Data

Create a new database named `countries.db` (make sure you're in the `data` folder):

```shell
> sqlite3 countries.db
```
Within the SQLite prompt, set the mode to CSV and import data from `countries.csv` into a table named `countries`:

```shell
sqlite> .mode csv
sqlite> .import countries.csv countries
```

### 3. Check the Database Schema

View the structure of your database and tables:
```shell
sqlite> .schema
```

### 4. Display All Rows in the Table

Retrieve all records from the `countries` table:
```sql
SELECT * FROM countries;
```

### 5. Select Capital Cities

List all capital cities:
```sql
SELECT capital FROM countries;
```

### 6. Find the Maximum Population

Identify the highest population among all countries:

```sql
SELECT MAX(population) FROM countries; -- Something seems not right.
```

### 7. Restart and Recreate the Table

If you need to start over, you can drop the existing table and recreate it:

```sql
DROP TABLE countries;

CREATE TABLE countries(code TEXT, name TEXT, continent TEXT, population INTEGER, capital TEXT);
```
Set the mode to CSV and import the data again:
```shell
.mode csv
.import countries.csv countries
```

### 8. Delete the Header Row

If the CSV headers were imported as data, delete the first row:

```sql
DELETE FROM countries WHERE code = 'code';
```
Now you can find correct maximum population
```sql
SELECT MAX(population) FROM countries;
```

### 9. Configure Output Formatting

Enable headers and set the output mode to column for better readability:

```shell
.headers on
.mode column
```

Display the data with the new settings:

```sql
SELECT * FROM countries;
```

### 10. Find the Total Number of Rows

Get the total count of countries:

```sql
SELECT COUNT(*) FROM countries;
```

### 11. Find Continents

List all continents represented in the table:

```sql
SELECT continent FROM countries;

-- Better

SELECT DISTINCT(continent) FROM countries;
```

Count the number of distinct continents:

```sql
--- How many:
SELECT COUNT(DISTINCT(continent)) FROM countries;
```

### 12. Count the Number of Asian Countries

Find the number of countries in Asia:

```sql
SELECT COUNT(*) FROM countries WHERE continent = 'Asia';
```

### 13. Find Continents and Country Counts

Get the number of countries per continent:

```sql
SELECT continent, COUNT(*) as total
FROM countries
GROUP BY continent
ORDER BY total;
```

To sort the results from highest to lowest:

```sql
SELECT continent, COUNT(*) as total
FROM countries
GROUP BY continent
ORDER BY total DESC;
```

### 14. Find the Continent with the Most Countries

Retrieve the continent with the highest number of countries:

```sql
SELECT continent, COUNT(*) as total
FROM countries 
GROUP BY continent
ORDER BY total DESC
LIMIT 1;
```

### 15. Perform Pattern Matching Searches (Vague Searches)

Find countries whose names start with 'U':

```sql
SELECT name
FROM countries 
WHERE name LIKE 'U%';
```

Find countries where the third letter is 'i':

```sql
SELECT name
FROM countries 
WHERE name LIKE '__i%'; -- third letter is i
```

### 16. Insert Data

Add a new country to the table:

```sql
INSERT INTO countries (code, name, continent) VALUES('CA', 'Canada', 'North America');
```

### 17. Update Data (Use with Caution)

Update the capital of `Canada`:

```sql
UPDATE countries 
SET capital='Ottawa'
WHERE name='Canada'; -- What if I forget this WHERE clause?
```

**Warning: Omitting the WHERE clause will update the capital for all countries.**

### 18. Delete Data (Use with Caution)

Remove `Canada` from the table:

```sql
DELETE FROM countries 
WHERE name='Canada';
```

**Warning: Omitting the WHERE clause will delete all records from the table.**

### 19. Rollback Changes (Transactions)

To **undo** the last change (insert, update, or delete):

```sql
BEGIN; -- Start a transaction
DELETE FROM countries WHERE name='Canada'; -- Delete Canada
SELECT * FROM countries WHERE name='Canada'; -- Verify the change
ROLLBACK; -- Undo the last change
```

If you're satisfied with the change, you can **commit** it:

```sql
BEGIN; -- Start a transaction
DELETE FROM countries WHERE name='Canada'; -- Delete Canada
SELECT * FROM countries WHERE name='Canada'; -- Verify the change
COMMIT; -- Save the change
```

To learn more about **transactions**, refer to the [SQLite documentation](https://www.sqlite.org/transactional.html).

## IMDB Example (shows.db)

### 1. Open the Database

Open the `shows.db` database:

```shell
> sqlite3 shows.db
```

Within the SQLite prompt, check the schema and set output formatting:

```sql
.schema

.headers on
.mode column
```

### 2. Basic Select Queries

Retrieve records from the `shows` table:

```sql
SELECT * FROM shows;
SELECT * FROM shows LIMIT 10;
```

### 3. Working with Foreign Keys: `shows`, `genres`, and `stars` tables

List the first 10 records from the `stars` table (which contains foreign keys):

```sql
SELECT * FROM stars LIMIT 10;
```

Find all shows categorized under `'Comedy'`:

```sql
SELECT * FROM genres WHERE genre = 'Comedy';
```

Retrieve details of a specific show by ID:

```sql
SELECT * FROM shows WHERE id = 65283;
```
Get `show_ids` for comedies:

```sql
SELECT show_id FROM genres WHERE genre = 'Comedy' LIMIT 10;
```

List titles of all shows that are comedies:

```sql
SELECT title
FROM shows
WHERE id IN (
    SELECT show_id
    FROM genres
    WHERE genre = 'Comedy'
)
ORDER BY title;
```

Find people whose names start with `'Steve'`:

```sql
SELECT * FROM people WHERE name LIKE 'Steve %';
```

List titles of shows starring `'Steve Carell'`:

```sql
SELECT title
FROM shows
WHERE id IN (
    SELECT show_id
    FROM stars
    WHERE person_id = (
        SELECT id
        FROM people
        WHERE name = 'Steve Carell'
    )
);
```

### 4. Using JOINs

Retrieve all information about `'The Office'` by joining `shows` and `genres`:

```sql
SELECT *
FROM shows
JOIN genres ON shows.id = genres.show_id
WHERE title = 'The Office';
```

Join `shows` and `ratings` to get rating information for `'The Office'`:

```sql
SELECT *
FROM shows
JOIN ratings ON shows.id = ratings.show_id
WHERE title = 'The Office';
```

### 5. JOINs: Explicit vs. Implicit

Explicit JOIN:

```sql
SELECT title
FROM people
JOIN stars ON people.id = stars.person_id
JOIN shows ON stars.show_id = shows.id
WHERE name = 'Steve Carell';
```

Implicit JOIN:

```sql
SELECT title
FROM people, stars, shows
WHERE people.id = stars.person_id
  AND stars.show_id = shows.id
  AND name = 'Steve Carell';
```

### 6. Using Indexes to Improve Performance

Enable the timer to measure query execution time:

```sql
.timer ON
```
Run a query to select shows with the title 'The Office':

```sql
SELECT * FROM shows WHERE title = 'The Office';
```

Create an index on the title column in the shows table:

```sql
CREATE INDEX title_index ON shows (title);
```

Run the query again to see improved performance:

```sql
SELECT * FROM shows WHERE title = 'The Office';
```

### 7. Indexing for Complex Queries

Before creating indexes:

```sql
SELECT title
FROM people
JOIN stars ON people.id = stars.person_id
JOIN shows ON stars.show_id = shows.id
WHERE name = 'Steve Carell';
```

Create indexes to optimize the query:

```sql
CREATE INDEX person_index ON stars (person_id);
CREATE INDEX show_index ON stars (show_id);
CREATE INDEX name_index ON people (name);
```

Run the query again to see performance improvements:

```sql
SELECT title
FROM people
JOIN stars ON people.id = stars.person_id
JOIN shows ON stars.show_id = shows.id
WHERE name = 'Steve Carell';
```
