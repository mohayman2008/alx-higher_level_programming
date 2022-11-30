-- This script creates the database hbtn_0c_0 in the MySQL server if it's not existing

-- Creates the database hbtn_0c_0 in the MySQL server if it's not existing
SELECT `city`, AVG(`value`) as 'avg_temp'
FROM `temperatures`
GROUP BY `city`
ORDER BY AVG(`value`) DESC;
