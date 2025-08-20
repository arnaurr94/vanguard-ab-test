USE vanguard;
    
-- How many sessions are there per new or long standing client?
 SELECT 
  FLOOR(c.tenure_yr / 10) * 10 AS tenure_range_start,
  FLOOR(c.tenure_yr / 10) * 10 + 9 AS tenure_range_end,
  COUNT(*) AS count_clients,
  variation
from `session` s
join clients c on c.client_id = s.client_id
join participants p on p.client_id = s.client_id
GROUP BY tenure_range_start, tenure_range_end, variation
ORDER BY tenure_range_start ASC;

-- How many sessions are there per age range?
SELECT
    FLOOR(c.age / 10) * 10 AS age_range_start,
    FLOOR(c.age / 10) * 10 + 9 AS age_range_end,
    COUNT(*) AS count_clients,
    variation
from `session` s
join clients c on c.client_id = s.client_id
join participants p on p.client_id = s.client_id
GROUP BY age_range_start, age_range_end, variation
ORDER BY age_range_start DESC;