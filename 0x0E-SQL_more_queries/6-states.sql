-- 6-create_db_and_table_states.sql
-- Script to create the database 'hbtn_0d_usa' and the table 'states' with specified columns

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

