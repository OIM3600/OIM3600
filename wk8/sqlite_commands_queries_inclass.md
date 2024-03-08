# countries example

0. Enter sqlite3
```
sqlite3
```

1. Quit sqlite3
```
sqlite> .exit
```

2. Create db under `data` folder
```
sqlite3 countries.db


sqlite> .mode csv
sqlite> .import countries.csv countries
```
3. Check schema
```
sqlite> .schema
```

4. Show all in the table
```sql
sqlite> SELECT * FROM countries;
```

5. Select capital cities
```sql
sqlite> SELECT capital FROM countries;
```

6. Find max population
```sql
sqlite> SELECT MAX(population) FROM countries;
```

7. Start Over
```
sqlite> .exit

sqlite3 countries.db

sqlite> DROP TABLE countries;

sqlite> CREATE TABLE countries(code TEXT, name TEXT, continent TEXT, population INTEGER, capital TEXT);

sqlite> .mode csv
sqlite> .import countries.csv countries
```

8. Need to delete first row
```sql
sqlite> DELETE FROM countries WHERE code = 'code';

-- Now you can find max
sqlite> SELECT MAX(population) FROM countries;
```

9. Turn headers on; turn column mode on;
```sql
sqlite> .headers on
sqlite> .mode column

sqlite> SELECT * FROM countries;
```

10. Find total # of rows
```sql
sqlite> SELECT COUNT(*) FROM countries;
```

11. Find continents
```sql
sqlite> SELECT continent FROM countries;

-- Better

sqlite> SELECT DISTINCT(continent) FROM countries;

--- How many:
sqlite> SELECT COUNT(DISTINCT(continent)) FROM countries;
```

12. How many Asian countries?
```sql
sqlite> SELECT COUNT(*) FROM countries WHERE continent = 'Asia';
```


13. Find continents and count
```sql
sqlite> SELECT continent, COUNT(*) as total
      > FROM countries 
      > GROUP BY continent
      > ORDER BY total; -- DESC
```

14. No.1 
```sql
sqlite> SELECT continent, COUNT(*) as total
      > FROM countries 
      > GROUP BY continent
      > ORDER BY total DESC
      > LIMIT 1;
```

15. Vague search
```sql
sqlite> SELECT name
      > FROM countries 
      > WHERE name LIKE 'U%';

sqlite> SELECT name
      > FROM countries 
      > WHERE name LIKE '__i%'; -- third letter is i
```

16. Insert data
```sql
sqlite> INSERT INTO countries (code, name, continent) VALUES('CA', 'Canada', 'North America');
```

17. Update (could be very dangerous)
```sql
sqlite> UPDATE countries 
      > SET capital='Ottawa'
      > WHERE name='Canada'; -- What if I forget this WHERE clause?
```

18. DELETE (even more dangerous)
```sql
sqlite> DELETE FROM countries WHERE name='Canada';
```


# IMDB

1. shows.db
```
sqlite3 shows.db

sqlite> .schema

sqlite> .headers on
sqlite> .mode column
```

2. Select Queries
```sql
sqlite> SELECT * FROM shows;
sqlite> SELECT * FROM shows LIMIT 10;
```

3. Foreign key, Using shows and genres

```sql
sqlite> SELECT * FROM stars LIMIT 10; -- Foreign keys

sqlite> SELECT * FROM genres WHERE genre = 'Comedy';

sqlite> SELECT * FROM shows WHERE id=65283;

sqlite> SELECT show_id FROM genres WHERE genre = 'Comedy' LIMIT 10;

sqlite> SELECT title 
      > FROM shows 
      > WHERE id IN (
      >     SELECT show_id 
      >     FROM genres 
      >     WHERE genre = 'Comedy'
      >     ) 
      > ORDER BY title;

sqlite> SELECT * FROM people WHERE name LIKE 'Steve %';

sqlite> SELECT title 
      > FROM shows 
      > WHERE id IN (
      >     SELECT show_id 
      >     FROM stars 
      >     WHERE person_id = (
      >         SELECT id 
      >         FROM people 
      >         WHERE name = 'Steve Carell'
      >         )
      >     );

```

4. Join
```sql
sqlite> SELECT * 
      > FROM shows JOIN genres 
      > ON shows.id = genres.show_id 
      > WHERE title = 'The Office';

sqlite> SELECT * 
      > FROM shows JOIN ratings 
      > ON shows.id = ratings.show_id 
      > WHERE title = 'The Office';
```

5. JOIN, with/without using ON
```sql

-- Explicit JOIN
sqlite> SELECT title 
      > FROM people JOIN stars 
      > ON people.id = stars.person_id 
      > JOIN shows ON stars.show_id = shows.id 
      > WHERE name = 'Steve Carell';

-- Implicit JOIN
sqlite> SELECT title 
      > FROM people, stars, shows 
      > WHERE people.id = stars.person_id AND stars.show_id = shows.id AND name = 'Steve Carell';
```

6. Index
```sql
sqlite> .timer ON
sqlite> SELECT * FROM shows WHERE title = 'The Office';


-- Create index
sqlite> CREATE INDEX title_index ON shows (title);

sqlite> SELECT * FROM shows WHERE title = 'The Office';
```

7. One more index example
```sql
sqlite> SELECT title FROM people 
      > JOIN stars ON people.id = stars.person_id 
      > JOIN shows ON stars.show_id = shows.id 
      > WHERE name = 'Steve Carell';

sqlite> CREATE INDEX person_index ON stars (person_id);

sqlite> CREATE INDEX show_index ON stars (show_id);

sqlite> CREATE INDEX name_index ON people (name);

sqlite> SELECT title FROM people 
      > JOIN stars ON people.id = stars.person_id 
      > JOIN shows ON stars.show_id = shows.id 
      > WHERE name = 'Steve Carell';
```





