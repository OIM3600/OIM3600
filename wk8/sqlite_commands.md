# countries example

1. Enter sqlite3
```
sqlite3
```
2. create db under `data` folder
```
sqlite3 countries.db


sqlite> .mode csv
sqlite> .import countries.csv countries
```
3. Check schema
```
sqlite> .schema
```

4. Show all rows in the table
```sql
SELECT * FROM countries;
```

5. Select capital cities
```sql
SELECT capital FROM countries;
```

6. Find max population
```sql
SELECT MAX(population) FROM countries;
```

7. Start Over
`sqlite3 countries.db`
```sql
DROP TABLE countries;

CREATE TABLE countries(code TEXT, name TEXT, continent TEXT, population INTEGER, capital TEXT);

.mode csv
.import countries.csv countries
```

8. Need to delete first row
```sql
DELETE FROM countries WHERE code = 'code';

-- Now you can find max
SELECT MAX(population) FROM countries;
```

9. Turn headers on; turn column mode on;
```
.headers on
.mode column
```
```sql
SELECT * FROM countries;
```

10. Find total # of rows
```sql
SELECT COUNT(*) FROM countries;
```

11. Find continents
```sql
SELECT continent FROM countries;

-- Better

SELECT DISTINCT(continent) FROM countries;

--- How many:
SELECT COUNT(DISTINCT(continent)) FROM countries;
```

12. How many Asian countries?
```sql
SELECT COUNT(*) FROM countries WHERE continent = 'Asia';
```


13. Find continents and count
```sql
SELECT continent, COUNT(*) as total
FROM countries 
GROUP BY continent
ORDER BY total; -- DESC
```

14. No.1 
```sql
SELECT continent, COUNT(*) as total
FROM countries 
GROUP BY continent
ORDER BY total DESC
LIMIT 1;
```

15. Vague search
```sql
SELECT name
FROM countries 
WHERE name LIKE 'U%';

SELECT name
FROM countries 
WHERE name LIKE '__i%'; -- third letter is i
```

16. Insert data
```sql
INSERT INTO countries (code, name, continent) VALUES('CA', 'Canada', 'North America');
```

17. Update (could be very dangerous)
```sql
UPDATE countries 
SET capital='Ottawa'
WHERE name='Canada'; -- What if I forget this WHERE clause?
```

18. DELETE (even more dangerous)
```sql
DELETE FROM countries WHERE name='Canada';
```


# IMDB

1. shows.db
```
sqlite3 shows.db

.schema

.headers on
.mode column
```

2. Select Queries
```sql
SELECT * FROM shows;
SELECT * FROM shows LIMIT 10;
```

3. Foreign key, Using shows and genres

```sql
SELECT * FROM stars LIMIT 10; -- Foreign keys

SELECT * FROM genres WHERE genre = 'Comedy';

SELECT * FROM shows WHERE id=65283;

SELECT show_id FROM genres WHERE genre = 'Comedy' LIMIT 10;

SELECT title 
FROM shows 
WHERE id IN (
    SELECT show_id 
    FROM genres 
    WHERE genre = 'Comedy'
    ) 
ORDER BY title;

SELECT * FROM people WHERE name LIKE 'Steve %';

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

4. Join
```sql
SELECT * 
FROM shows JOIN genres 
ON shows.id = genres.show_id 
WHERE title = 'The Office';

SELECT * 
FROM shows JOIN ratings 
ON shows.id = ratings.show_id 
WHERE title = 'The Office';
```

5. JOIN, with/without using ON
```sql

-- Explicit JOIN
SELECT title 
FROM people JOIN stars 
ON people.id = stars.person_id 
JOIN shows ON stars.show_id = shows.id 
WHERE name = 'Steve Carell';

-- Implicit JOIN
SELECT title 
FROM people, stars, shows 
WHERE people.id = stars.person_id AND stars.show_id = shows.id AND name = 'Steve Carell';
```

6. Index
```sql
.timer ON
SELECT * FROM shows WHERE title = 'The Office';


-- Create index
CREATE INDEX title_index ON shows (title);

SELECT * FROM shows WHERE title = 'The Office';
```

7. One more index example
```sql
SELECT title FROM people 
JOIN stars ON people.id = stars.person_id 
JOIN shows ON stars.show_id = shows.id 
WHERE name = 'Steve Carell';

CREATE INDEX person_index ON stars (person_id);

CREATE INDEX show_index ON stars (show_id);

CREATE INDEX name_index ON people (name);

SELECT title FROM people 
JOIN stars ON people.id = stars.person_id 
JOIN shows ON stars.show_id = shows.id 
WHERE name = 'Steve Carell';
```





