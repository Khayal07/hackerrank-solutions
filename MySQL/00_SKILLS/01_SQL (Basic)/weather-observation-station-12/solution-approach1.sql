-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true
-- Problem     Weather Observation Station 12
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-17, 06:53 p.m.
-- ──────────────────────────────────────────────────

select distinct city
from station
where left(city, 1) not in ('a', 'e', 'i', 'o', 'u') and
      right(city, 1) not in ('a', 'e', 'i', 'o', 'u')
