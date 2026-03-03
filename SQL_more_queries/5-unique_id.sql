-- Create the table unique_id
create table if not exists unique_id (
    id int default 1 unique,
    name varchar(256)
)