-- List the number of records with the same score in the second_table.
select score, count(*) as number from second_table group by score;