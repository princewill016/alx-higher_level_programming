-- 15-comedy_shows.sql
-- Script to list all Comedy shows in the database

SELECT t.title
FROM tv_shows t
JOIN tv_show_genres sg ON t.id = sg.tv_show_id
JOIN genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY t.title ASC;

