-- This script list all genres not linked to the show 'Dexter'
-- according to the database 'hbtn_0d_tvshows'

-- The query
SELECT g.`name`
FROM `tv_shows` AS s
	INNER JOIN `tv_show_genres` AS sg
	ON sg.`show_id` = s.`id`
	AND s.`title` = 'Dexter'
		RIGHT JOIN `tv_genres` AS g
		ON sg.`genre_id` = g.`id`
WHERE s.`title` IS NULL
ORDER BY g.`name` ASC;

/*
SELECT `name`
FROM `tv_genres`
WHERE `name` NOT IN
	(
		SELECT g.`name`
		FROM `tv_genres` AS g
			INNER JOIN `tv_show_genres` AS sg
			ON sg.`genre_id` = g.`id`
				INNER JOIN `tv_shows` AS s
				ON sg.`show_id` = s.`id`
				AND s.`title` = 'Dexter'
	)
ORDER BY `name` ASC;
*/
