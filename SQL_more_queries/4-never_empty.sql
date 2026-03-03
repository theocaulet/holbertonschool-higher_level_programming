-- Create the table id_not_null
create table if not exists id_not_null (
    id int default 1,
    name varchar(256)
)