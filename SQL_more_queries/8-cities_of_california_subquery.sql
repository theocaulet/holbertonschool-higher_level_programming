-- Lists all the cities of California in the database hbtn_0d_usa.
select * from cities
where state_id = (select id from states where name = 'California')
order by cities.id;