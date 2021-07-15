-- imp table dumb
-- display top 3 avg temp by city during July & August sort by temp desc
SELECT city, AVG(value)
AS avg_temp
FROM temperatures
WHERE month = 7
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
