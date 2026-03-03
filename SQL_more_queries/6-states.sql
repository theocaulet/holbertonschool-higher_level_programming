-- Create the database 'hbtn_0d_usa' and the table 'states'.
create database if not exists hbtn_0d_usa;
use hbtn_0d_usa;
create table if not exists states (
    id int unique auto_increment primary key,
    name varchar(256) not null
)