-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
-- Problem     Contest Leaderboard
-- Difficulty  Medium
-- Subdomain   Basic Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-24, 09:24 p.m.
-- ──────────────────────────────────────────────────

select h.hacker_id, 
       h.name, sum(m.max_score) as total_score
from hackers h
join (
    select hacker_id, challenge_id, max(score) as max_score
    from submissions
    group by hacker_id, challenge_id
) m on h.hacker_id = m.hacker_id
group by h.hacker_id, h.name
having total_score > 0
order by total_score desc, h.hacker_id asc;
