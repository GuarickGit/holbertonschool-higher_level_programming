-- Script that lists all records with a score >= 10 from second_table ordered by score (top first)
-- Selecting score and name, ordered by highest score first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC, name
