-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
-- Problem     Weather Observation Station 5
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-13, 03:16 a.m.
-- ──────────────────────────────────────────────────

select city,
       length(city)
from station
order by length(city) asc, city asc
limit 1;

select city,
       length(city)
from station
order by length(city) desc, city desc
limit 1;
