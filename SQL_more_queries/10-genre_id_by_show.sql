-- Lists all shows contained in hbtn_0_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0_tvshows tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;