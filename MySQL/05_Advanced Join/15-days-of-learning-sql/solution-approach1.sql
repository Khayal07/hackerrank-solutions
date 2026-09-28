-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true
-- Problem     15 Days of Learning SQL
-- Difficulty  Hard
-- Subdomain   Advanced Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-28, 07:23 p.m.
-- ──────────────────────────────────────────────────

with dailymaxhacker as (
    select submission_date,
           hacker_id,
           row_number() over(
            partition by submission_date
            order by count(submission_id) desc, hacker_id asc
           ) as rn 
    from submissions
    group by submission_date, hacker_id
),


everydayhackers as (
    select s1.submission_date,
           count(distinct s1.hacker_id) as consecutive_hackers
    from submissions s1
    where (
        select count(distinct s2.submission_date)
        from submissions s2
        where s2.hacker_id = s1.hacker_id
        and s2.submission_date <= s1.submission_date
    ) = datediff(s1.submission_date, '2016-03-01') + 1
    group by s1.submission_date
)


select e.submission_date,
       e.consecutive_hackers,
       m.hacker_id,
       h.name
from everydayhackers e
join dailymaxhacker m on e.submission_date = m.submission_date and m.rn = 1
join hackers h on m.hacker_id = h.hacker_id
order by e.submission_date asc;
