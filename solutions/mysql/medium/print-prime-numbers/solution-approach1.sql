-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
-- Problem     Print Prime Numbers
-- Difficulty  Medium
-- Subdomain   Alternative Queries
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-28, 07:34 p.m.
-- ──────────────────────────────────────────────────

with recursive numbers as (
    select 2 as n
    union all
    select n + 1
    from numbers
    where n < 1000
)

select group_concat(n1.n separator '&')
from numbers n1
where not exists (
    select 1
    from numbers n2
    where n2.n < n1.n and n1.n %n2.n = 0
);
