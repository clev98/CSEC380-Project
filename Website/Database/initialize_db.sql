CREATE DATABASE IF NOT EXISTS Application;


use Application;

CREATE TABLE User_Login
(
	Username VARCHAR(255),
	password_hash_salt VARBINARY(64),
	PRIMARY KEY(Username)
);
CREATE TABLE Video_files
(
	Video_ID INT,
	Owner VARCHAR(64),
	Path_To_Video VARCHAR(64),
	Path_To_Thumbnail VARCHAR(64),
	PRIMARY KEY(Video_ID)
);

