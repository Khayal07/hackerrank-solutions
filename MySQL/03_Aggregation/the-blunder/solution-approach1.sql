-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
-- Problem     The Blunder
-- Difficulty  Easy
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-19, 06:56 p.m.
-- ──────────────────────────────────────────────────

select ceil(avg(salary) - avg(replace(salary, 0, '')))
from employees;
