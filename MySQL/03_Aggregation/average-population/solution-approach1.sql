-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true
-- Problem     Average Population
-- Difficulty  Easy
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-19, 06:51 p.m.
-- ──────────────────────────────────────────────────

select round(avg(population))
from city;
