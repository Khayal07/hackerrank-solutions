-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
-- Problem     Average Population of Each Continent
-- Difficulty  Easy
-- Subdomain   Basic Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-22, 10:50 p.m.
-- ──────────────────────────────────────────────────

select cn.continent,
       floor(avg(c.population))
from city c
join country cn on c.countrycode = cn.code
group by cn.continent;
