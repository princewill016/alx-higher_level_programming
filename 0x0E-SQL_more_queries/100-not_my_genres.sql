-- 17-genres_not_linked_to_dexter.sql
-- Script to list genres not linked to the show "Dexter"

SELECT g.name
FROM genres g
WHERE g.id NOT IN (
    SELECT sg.genre_id
    FROM tv_show_genres sg
    JOIN tv_shows t ON sg.tv_show_id = t.id
    WHERE t.title = 'Dexter'
)
ORDER BY g.name ASC;

