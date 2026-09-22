-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true
-- Problem     Population Census 
-- Difficulty  Easy
-- Subdomain   Basic Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-22, 10:43 p.m.
-- ──────────────────────────────────────────────────

select sum(c.population)
from city c
join country cn on c.countrycode = cn.code
where cn.continent = 'Asia';
