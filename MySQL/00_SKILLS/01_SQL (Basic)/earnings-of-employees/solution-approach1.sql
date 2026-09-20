-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
-- Problem     Top Earners
-- Difficulty  Easy
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-21, 01:40 a.m.
-- ──────────────────────────────────────────────────

select (salary * months), count(*)
from employee
group by (salary * months)
order by (salary * months) desc
limit 1;
