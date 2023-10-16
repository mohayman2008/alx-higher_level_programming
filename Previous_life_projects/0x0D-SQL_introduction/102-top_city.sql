-- This script displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending) in 'temperatures' table

-- Execute the query
SELECT `city`, AVG(`value`) as 'avg_temp'
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY AVG(`value`) DESC
LIMIT 3;
