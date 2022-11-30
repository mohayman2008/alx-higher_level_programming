-- This script creates the database hbtn_0c_0 in the MySQL server if it's not existing

-- Creates the database hbtn_0c_0 in the MySQL server if it's not existing
SELECT `state`, MAX(`value`) as 'max_temp'
FROM `temperatures`
GROUP BY `state`
ORDER BY (`state`) ASC;
