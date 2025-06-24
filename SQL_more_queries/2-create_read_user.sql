-- creates the database hbtn_0d_2 in my MySQL server, If the database hbtn_0d_2 already exists, the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the MySQL user 'user_0d_2'@'localhost' with the password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants select privilege on all databases and tables to 'user_0d_2'@'localhost'
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
