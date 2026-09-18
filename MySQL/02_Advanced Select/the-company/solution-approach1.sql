-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
-- Problem     New Companies
-- Difficulty  Medium
-- Subdomain   Advanced Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-18, 02:02 p.m.
-- ──────────────────────────────────────────────────

select c.company_code,
       c.founder,
       count(distinct lm.lead_manager_code),
       count(distinct sm.senior_manager_code),
       count(distinct m.manager_code),
       count(distinct e.employee_code)
from company c
left join lead_manager lm on c.company_code = lm.company_code
left join senior_manager sm on c.company_code = sm.company_code
left join manager m on c.company_code = m.company_code
left join employee e on c.company_code = e.company_code
group by c.company_code, c.founder
order by c.company_code
