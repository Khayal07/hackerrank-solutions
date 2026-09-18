-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
-- Problem     Occupations
-- Difficulty  Medium
-- Subdomain   Advanced Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-18, 01:51 p.m.
-- ──────────────────────────────────────────────────

with RankedOccupations as (
    select name,
           occupation,
           row_number() over(partition by occupation order by name) as RowNum
           from occupations
)

select 
    max(case when occupation = 'Doctor' then name end) as Doctor,
    max(case when occupation = 'Professor' then name end) as Professor,
    max(case when occupation = 'Singer' then name end) as Singer,
    max(case when occupation = 'Actor' then name end) as Actor
from RankedOccupations
group by RowNum
order by RowNum;
