-- This script creates the database 'hbtn_0d_usa' in the MySQL server if it's not existing
-- and creates table 'cities' if it's not already existing

-- Create the database 'hbtn_0d_usa'
CREATE DATABASE
IF NOT EXISTS
`hbtn_0d_usa`;

-- Select the database 'hbtn_0d_usa'
USE `hbtn_0d_usa`;

-- Create table 'cities'
CREATE TABLE
IF NOT EXISTS `cities`
(
    `id` INT
    UNIQUE
    PRIMARY KEY
    NOT NULL
    AUTO_INCREMENT,

    `state_id` INT
    NOT NULL,

    FOREIGN KEY(`state_id`)
    REFERENCES `states`(`id`),
    
    `name` VARCHAR(256)
    NOT NULL
);
