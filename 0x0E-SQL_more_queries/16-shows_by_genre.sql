-- 16-all_shows_and_genres.sql
-- Script to list all shows and their linked genres from the database hbtn_0d_tvshows

SELECT t.title, g.name AS genre
FROM tv_shows t
LEFT JOIN tv_show_genres sg ON t.id = sg.tv_show_id
LEFT JOIN genres g ON sg.genre_id = g.id
ORDER BY t.title ASC, g.name ASC;

