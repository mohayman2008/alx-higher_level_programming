-- This script converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Select Database 'hbtn_0c_0'
USE `hbtn_0c_0`;

-- Convert Database
ALTER DATABASE `hbtn_0c_0`
CHARSET=utf8mb4 
COLLATE=utf8mb4_unicode_ci;

-- Convert Table
ALTER TABLE `first_table`
CHARSET=utf8mb4 
COLLATE=utf8mb4_unicode_ci;

---- ALTER TABLE `first_table` ----
-- CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
