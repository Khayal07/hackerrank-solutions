-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
-- Problem     Weather Observation Station 7
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-16, 02:01 p.m.
-- ──────────────────────────────────────────────────

select distinct city
from station
where right(city, 1) in ('a', 'e', 'i', 'o', 'u')
