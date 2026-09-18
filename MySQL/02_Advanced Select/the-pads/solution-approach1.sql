-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
-- Problem     The PADS
-- Difficulty  Medium
-- Subdomain   Advanced Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-18, 01:43 p.m.
-- ──────────────────────────────────────────────────

select concat(Name, '(', left(Occupation, 1), ')')
from occupations
order by Name;



select concat('There are a total of ', count(*), ' ', lower(Occupation), 's.')
from occupations
group by Occupation
order by count(*), Occupation;
