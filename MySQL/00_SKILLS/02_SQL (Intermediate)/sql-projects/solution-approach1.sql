-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
-- Problem     SQL Project Planning
-- Difficulty  Medium
-- Subdomain   Advanced Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-25, 04:47 p.m.
-- ──────────────────────────────────────────────────

select s.start_date,
       min(e.end_date)
from(
    select start_date
    from projects
    where start_date not in (select end_date from projects)
) s
join (
    select end_date
    from projects
    where end_date not in (select start_date from projects)
) e on s.start_date < e.end_date
group by s.start_date
order by datediff(min(e.end_date), s.start_date) asc, s.start_date asc;
