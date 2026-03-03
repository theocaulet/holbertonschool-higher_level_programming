-- Create the MySQL server user 'user_0d_1'
create user if not exists 'user_0d_1'@'%' identified by 'user_0d_1_pwd';
grant all privileges on *.* to 'user_0d_1'@'%';