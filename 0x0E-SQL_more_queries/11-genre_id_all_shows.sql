-- 11-list_all_shows_with_genres.sql
-- Script to list all TV shows, including those without a genre linked

-- Select tv_shows.title and tv_show_genres.genre_id, displaying NULL if no genre is linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

