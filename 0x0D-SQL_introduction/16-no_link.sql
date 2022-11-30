-- This script shows all the records of 'second_table' where 'name' != NULL

-- Query the data
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
