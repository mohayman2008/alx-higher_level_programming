-- This script displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending) in 'temperatures' table

-- Execute the query
SELECT `city`, AVG(`value`) as 'avg_temp'
FROM `temperatures`
WHERE `month` IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
