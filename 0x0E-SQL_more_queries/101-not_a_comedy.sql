-- 100-not_my_genres.sql
-- Script to list all shows without the genre "Comedy"

SELECT t.title
FROM tv_shows t
WHERE t.id NOT IN (
    SELECT sg.tv_show_id
    FROM tv_show_genres sg
    JOIN tv_genres g ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
)
ORDER BY t.title ASC;

