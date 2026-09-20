-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true
-- Problem     Weather Observation Station 15
-- Difficulty  Easy
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-21, 01:50 a.m.
-- ──────────────────────────────────────────────────

select round(long_w, 4)
from station
where lat_n < 137.2345
order by lat_n desc
limit 1;
