-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true
-- Problem     Weather Observation Station 13
-- Difficulty  Easy
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-21, 01:45 a.m.
-- ──────────────────────────────────────────────────

select truncate(sum(lat_n), 4)
from station
where lat_n > 38.7880 and lat_n < 137.2345
