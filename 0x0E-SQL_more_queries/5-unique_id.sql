-- Script to create table unique_id

-- Create table unique_id if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
