CREATE DATABASE IF NOT EXISTS Application;


use Application;

CREATE TABLE User_Login
(
	Username VARCHAR(255),
    salt CHAR(16),
	password_hash_salt CHAR(56),
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

INSERT INTO User_Login (Username, salt, password_hash_salt) VALUES ("chaim", "pL41qCFwnagJcZsM", "f2094e7e7ce265f17fea0b8910206d9487ef37c0ee5fb8a676a42484")