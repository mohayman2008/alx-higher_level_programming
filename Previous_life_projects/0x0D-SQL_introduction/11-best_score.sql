-- This script show the records of 'second_table' sorted in descending order by 'score'
-- and filtered to show only records where score > 10

-- Query the data
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
