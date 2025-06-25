-- Lists all shows in the database that have at least one genre linked
-- Select shows that have at least one genre, with title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show
INNER JOIN tv_show_genres ON tv_show_genres.tv_show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
