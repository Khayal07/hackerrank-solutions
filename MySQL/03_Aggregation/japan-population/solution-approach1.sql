-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/japan-population/problem?isFullScreen=true
-- Problem     Japan Population
-- Difficulty  Easy
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-19, 06:52 p.m.
-- ──────────────────────────────────────────────────

select sum(population)
from city
where countrycode = 'JPN';
