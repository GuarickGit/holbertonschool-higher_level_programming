-- Script that creates the table id_not_null on my MySQL server
-- id value is 1 by default
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256),
);
