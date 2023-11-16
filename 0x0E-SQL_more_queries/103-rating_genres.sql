-- This script lists all genres in the database 'hbtn_0d_tvshows_rate' by their rating

-- The query
SELECT g.`name`,
	SUM(r.`rate`) AS 'rating'
FROM `tv_genres` as g
	INNER JOIN `tv_show_genres` AS sg
    ON g.`id` = sg.`genre_id`
		INNER JOIN `tv_show_ratings` as r
		ON r.`show_id` = sg.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC;
