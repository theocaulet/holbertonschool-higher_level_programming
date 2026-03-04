-- List all genres from hbtn_0d_tvshows.
SELECT tv.genre AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
JOIN genres AS tv ON tv_show_genres.genre_id = tv.id
GROUP BY genre
ORDER BY number_of_shows DESC, tv.genre ASC;