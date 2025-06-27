-- Lists all shows and their genres (NULL if no genre is linked)
SELECT tv_shows.title, tv_genres.name
-- Selects the title of the show and the name of the genre

FROM tv_shows
-- Start from the tv_shows table (we want to list all shows)

LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Left join with the association table to get genre links
-- LEFT JOIN ensures shows with no genre are still included

LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Join with the tv_genres table to get the genre names
-- If no genre is linked, this will return NULL

ORDER BY tv_shows.title ASC, tv_genres.name ASC;
-- Sort the results by show title (A-Z), then genre name (A-Z)
