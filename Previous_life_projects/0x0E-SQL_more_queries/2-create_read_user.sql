-- This script creates the database 'hbtn_0d_2' in the MySQL server if it's not existing
-- and creates a MySQL server user 'user_0d_2' if it's not already existing
-- and grants 'user_0d_2' SELECT privilages on 'hbtn_0d_2'

-- Creates the database hbtn_0d_2 in the MySQL server if it's not existing
CREATE DATABASE
IF NOT EXISTS
`hbtn_0d_2`;

-- Create the user 'user_0d_2'
CREATE USER 
IF NOT EXISTS 
'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT the privilages
GRANT SELECT
ON `hbtn_0d_2`.*
TO 'user_0d_2'@'localhost';
