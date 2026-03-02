-- Creates a new table called second_table.
create table if not exists second_table (
    id int,
    name varchar(256),
    score int
);
insert into second_table (id, name, score)
values (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);