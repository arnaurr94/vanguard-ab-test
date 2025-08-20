USE vanguard;

-- Completion Rate:
SELECT  p.variation, 
		count(*) AS number_completes
FROM `session` s
JOIN participants p
	ON p.client_id = s.client_id
GROUP BY p. variation, s.step_cum_sum
HAVING s.step_cum_sum = 4;

-- Average Time Spent on Each Step:
SELECT  p.variation, 
		s.step_cum_sum AS step, 
        ROUND(avg(s.time_diff), 0) AS 'average time (s)'
FROM `session` AS s
JOIN participants AS p
	ON p.client_id = s.client_id
WHERE s.step_diff = 1
GROUP BY p. variation, s.step_cum_sum
HAVING s.step_cum_sum >= 0
ORDER BY p.variation DESC, s.step_cum_sum ASC;


-- Error Rates per step:
SELECT  p.variation,
		s.process_step,
        COUNT(*) AS Number_of_errors
FROM `session` AS s
JOIN participants AS p
	ON p.client_id = s.client_id
WHERE (s.step_diff < 0) AND (s.step_diff != -4)
GROUP BY s.process_step, p.variation
ORDER BY p.variation DESC, s.process_step ASC;


