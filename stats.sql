SELECT url, code, COUNT(*) AS number, AVG(time) AS mean_time, MAX(time) AS slowest, MIN(time) as fastest
	FROM results
	GROUP BY url, code;