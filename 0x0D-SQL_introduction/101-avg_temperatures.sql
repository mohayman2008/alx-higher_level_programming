-- This script displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending) in 'temperatures' table

-- Execute the query
SELECT `city`, AVG(`value`) as 'avg_temp'
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
