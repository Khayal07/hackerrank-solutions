-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true
-- Problem     Draw The Triangle 1
-- Difficulty  Easy
-- Subdomain   Alternative Queries
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-28, 07:28 p.m.
-- ──────────────────────────────────────────────────

with recursive pattern as (
    select 20 as n
    union all
    select n - 1
    from pattern
    where n > 1
)

select repeat ('* ', n)
from pattern;
