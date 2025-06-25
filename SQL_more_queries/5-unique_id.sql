-- Script that creates the table unique_id on my MySQL server
-- id value is 1 by default and is unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
);
