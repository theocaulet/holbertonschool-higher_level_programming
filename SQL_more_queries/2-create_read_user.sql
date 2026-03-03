-- Create the database 'hbtn_0d_2' and the user 'user_0d_2'.
create database if not exists hbtn_0d_2;
create user if not exists 'user_0d_2'@'%' identified by 'user_0d_2_pwd';
grant select on hbtn_0d_2.* to 'user_0d_2'@'%';