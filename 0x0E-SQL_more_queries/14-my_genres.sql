-- 14-genres_by_show_dexter.sql
-- Script to list all genres linked to the show "Dexter"

SELECT g.name AS genre
FROM genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows t ON sg.tv_show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY g.name ASC;

