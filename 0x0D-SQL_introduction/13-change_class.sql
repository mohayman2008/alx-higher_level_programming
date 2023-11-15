-- This script deletes records from 'second_table' based on expression

-- Delete rows
DELETE 
FROM second_table
WHERE `score` <= 5;
