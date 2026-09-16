-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
-- Problem     Weather Observation Station 8
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-16, 02:02 p.m.
-- ──────────────────────────────────────────────────

select distinct city
from station
where left(city, 1) in ('a', 'e', 'i', 'o', 'u') and 
      right(city, 1) in ('a', 'e', 'i', 'o', 'u')
