-- This script lists the number of records with the same score in the table 'second_table'

-- Query
SELECT `score`, COUNT(`score`) as 'number'
FROM `second_table`
GROUP BY `score`
ORDER BY count(*) DESC;