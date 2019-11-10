CREATE DATABASE IF NOT EXISTS Application;

CREATE USER 'armtube'@'%' IDENTIFIED BY 'absolutely_totally_secure';
GRANT ALL PRIVILEGES ON Application.* TO 'armtube'@'%';

use Application;

CREATE TABLE User_Login
(
	Username VARCHAR(255),
    salt CHAR(16),
	password_hash_salt CHAR(64),
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

INSERT INTO User_Login (Username, salt, password_hash_salt) VALUES ("chaim", "pL41qCFwnagJcZsM", "8c0f5ab2947a5a03c5275599e8b1cff2f7f281d07702a4082fcafa239b621ad8");