-- This script lists all shows without the genre 'Comedy'
-- in the database 'hbtn_0d_tvshows'

-- The query
SELECT `title`
FROM `tv_shows`
WHERE `title` NOT IN
	(
		SELECT s.`title`
		FROM `tv_shows` AS s
			INNER JOIN `tv_show_genres` AS sg
			ON sg.`show_id` = s.`id`
				INNER JOIN `tv_genres` AS g
				ON sg.`genre_id` = g.`id`
		WHERE g.`name` = 'Comedy'
	)
ORDER BY `title` ASC;
