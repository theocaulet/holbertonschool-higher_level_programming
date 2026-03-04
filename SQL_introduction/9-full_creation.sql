-- Creates a new table called second_table.
CREATE TABLE IF NOT EXISTS second_table (
    ID INT,
    NAME VARCHAR(256),
    SCORE INT
);
INSERT INTO second_table (ID, NAME, SCORE)
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);