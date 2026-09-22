-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true
-- Problem     African Cities
-- Difficulty  Easy
-- Subdomain   Basic Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-22, 10:44 p.m.
-- ──────────────────────────────────────────────────

select c.name
from city c
join country cn on c.countrycode = cn.code
where cn.continent = 'Africa';
