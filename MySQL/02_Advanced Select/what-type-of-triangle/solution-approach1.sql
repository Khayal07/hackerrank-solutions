-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
-- Problem     Type of Triangle
-- Difficulty  Easy
-- Subdomain   Advanced Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-18, 01:38 p.m.
-- ──────────────────────────────────────────────────

select 
    case 
        when a + b <= c or a + c <= b or c + b <= a then "Not A Triangle"
        when a = b and b = c then "Equilateral"
        when a = b or a = c or b = c then "Isosceles"
        else "Scalene"
    end
from triangles
