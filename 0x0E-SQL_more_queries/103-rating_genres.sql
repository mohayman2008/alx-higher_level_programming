-- This script lists all genres in the database 'hbtn_0d_tvshows_rate' by their rating

-- The query
SELECT g.`name`,
	SUM(r.`rate`) AS 'rating'
FROM `tv_genres` AS g
	INNER JOIN `tv_show_genres` AS sg
    ON g.`id` = sg.`genre_id`
		INNER JOIN `tv_show_ratings` AS r
		ON r.`show_id` = sg.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC;
