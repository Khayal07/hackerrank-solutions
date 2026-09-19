-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
-- Problem     Binary Tree Nodes
-- Difficulty  Medium
-- Subdomain   Advanced Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-18, 01:54 p.m.
-- ──────────────────────────────────────────────────

select N,
    case 
        when P is null then 'Root'
        when N in (select P from bst where P is not null) then 'Inner'
        else 'Leaf'
    end
from bst
order by N;
