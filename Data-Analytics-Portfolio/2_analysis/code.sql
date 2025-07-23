-- 1. Most in-demand skills
SELECT 
    skills, 
    COUNT(*) AS demand_count
FROM jobs
WHERE skills IS NOT NULL
GROUP BY skills
ORDER BY demand_count DESC
LIMIT 5;

-- 2. Average salary by location
SELECT 
    location, 
    AVG(salary) AS avg_salary
FROM jobs
GROUP BY location
ORDER BY avg_salary DESC;