-- 10-list_shows_with_genres.sql
-- Script to list all TV shows with at least one linked genre

-- Select tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

