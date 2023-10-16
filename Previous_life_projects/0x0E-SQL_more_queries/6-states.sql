-- This script creates the database 'hbtn_0d_usa' in the MySQL server if it's not existing
-- and creates table 'states' if it's not already existing

-- Create the database 'hbtn_0d_usa'
CREATE DATABASE
IF NOT EXISTS
`hbtn_0d_usa`;

-- Select the database 'hbtn_0d_usa'
USE `hbtn_0d_usa`;

-- Create table 'states'
CREATE TABLE
IF NOT EXISTS `states`
(
    `id` INT
    UNIQUE
    PRIMARY KEY
    NOT NULL
    AUTO_INCREMENT,
    
    `name` VARCHAR(256) 
    NOT NULL
);
