-- 13-genres_with_show_count.sql
-- Script to list all genres with the number of shows linked to each

SELECT g.name AS genre, COUNT(sg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.name
HAVING COUNT(sg.tv_show_id) > 0
ORDER BY number_of_shows DESC;

