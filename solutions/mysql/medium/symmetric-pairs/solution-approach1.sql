-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true
-- Problem     Symmetric Pairs
-- Difficulty  Medium
-- Subdomain   Advanced Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-25, 04:57 p.m.
-- ──────────────────────────────────────────────────

select f1.x,
       f1.y
from functions f1
join functions f2 on f1.x = f2.y and f1.y = f2.x
group by f1.x, f1.y
having f1.x < f1.y or (f1.x = f1.y and count(*) > 1)
order by f1.x asc;
