-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
-- Problem     Challenges
-- Difficulty  Medium
-- Subdomain   Basic Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-24, 09:23 p.m.
-- ──────────────────────────────────────────────────

select h.hacker_id, 
       h.name, 
       count(c.challenge_id) as total_count
from hackers h
join challenges c on h.hacker_id = c.hacker_id
group by h.hacker_id, h.name
having total_count = (
    select max(cnt)
    from (
        select count(challenge_id) as cnt
        from challenges
        group by hacker_id
    ) sub1
)
or total_count in (
    select cnt
    from (
        select count(challenge_id) as cnt
        from challenges
        group by hacker_id
    ) sub2
    group by cnt
    having count(cnt) = 1
)
order by total_count desc, h.hacker_id asc;
