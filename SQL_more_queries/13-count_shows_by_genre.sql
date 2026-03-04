-- List all genres from hbtn_0d_tvshows.
SELECT genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
JOIN genres ON tv_show_genres.genre_id = genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;