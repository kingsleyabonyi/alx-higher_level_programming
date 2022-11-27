-- Creates the user with all privilages.
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILAGES ON ',' To 'user_0d_1'@'localhost;
