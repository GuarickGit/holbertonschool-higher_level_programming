-- Lists the number of records with the same score in second_table
-- for each score, sorted by the number of records (descending)
SELECT COUNT(*) AS number, score
FROM second_table
GROUP BY score
ORDER BY number DESC;
