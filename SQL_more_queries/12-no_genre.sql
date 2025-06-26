-- Lists all shows without a genre linked in the database
-- Displays: tv_shows.title - tv_show_genres.genre_id
-- Only shows with no genre (i.e., genre_id IS NULL) are listed
-- Results sorted by title and genre_id (both ascending)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
