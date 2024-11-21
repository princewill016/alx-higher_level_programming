-- Create force_name table with specified constraints
-- Ensures table creation doesn't fail if it already exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
