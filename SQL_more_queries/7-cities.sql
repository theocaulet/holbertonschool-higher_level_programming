-- Create the database 'hbtn_0d_usa' and the table 'cities'.
create database if not exists hbtn_0d_usa;
use hbtn_0d_usa;
create table if not exists cities (
    id int unique auto_increment primary key,
    state_id int not null,
    foreign key (state_id) references states(id),
    name varchar(256) not null
)