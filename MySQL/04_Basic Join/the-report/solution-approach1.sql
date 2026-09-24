-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
-- Problem     The Report
-- Difficulty  Medium
-- Subdomain   Basic Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-24, 12:53 a.m.
-- ──────────────────────────────────────────────────

select case when g.grade >= 8 then s.name else null end,
       g.grade,
       s.marks
from students s
join grades g on s.marks between g.min_mark and g.max_mark
order by g.grade desc, s.name asc, s.marks asc;
