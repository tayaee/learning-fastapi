CREATE USER 'test'@'localhost' IDENTIFIED BY 'test';
CREATE USER 'test'@'%' IDENTIFIED BY 'test';
GRANT ALL ON *.* TO 'test'@'localhost';
GRANT ALL ON *.* TO 'test'@'%';
FLUSH PRIVILEGES;