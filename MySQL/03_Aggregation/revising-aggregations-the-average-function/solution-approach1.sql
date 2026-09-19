-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true
-- Problem     Revising Aggregations - Averages
-- Difficulty  Easy
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-19, 06:49 p.m.
-- ──────────────────────────────────────────────────

select avg(population)
from city
where district = 'California'
