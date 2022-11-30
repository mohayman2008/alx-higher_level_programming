-- This script creates the database hbtn_0c_0 in the MySQL server if it's not existing

-- Creates the database hbtn_0c_0 in the MySQL server if it's not existing
SELECT `city`, AVG(`value`) as 'avg_temp'
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY AVG(`value`) DESC
LIMIT 3;
