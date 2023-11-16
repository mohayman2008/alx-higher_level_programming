-- This script lists all shows from database 'hbtn_0d_tvshows_rate' by their rating

-- The query
SELECT s.`title`,
	 SUM(r.`rate`) AS 'rating'
FROM `tv_shows` as s
	INNER JOIN `tv_show_ratings` as r
	ON s.`id` = r.`show_id`
GROUP BY s.`title`
ORDER BY `rating` DESC;
