-- 4-create_table_id_not_null.sql
-- Script to create the table 'id_not_null' with specified columns and default value for 'id'

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

