-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/draw-the-triangle-2/problem?isFullScreen=true
-- Problem     Draw The Triangle 2
-- Difficulty  Easy
-- Subdomain   Alternative Queries
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-28, 07:29 p.m.
-- ──────────────────────────────────────────────────

with recursive pattern as (
    select 1 as n
    union all
    select n + 1 
    from pattern 
    where n < 20
)
select repeat('* ', n) 
from pattern;
