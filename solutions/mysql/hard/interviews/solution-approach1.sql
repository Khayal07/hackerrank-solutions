-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
-- Problem     Interviews
-- Difficulty  Hard
-- Subdomain   Advanced Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-25, 05:12 p.m.
-- ──────────────────────────────────────────────────

select c.contest_id,
       c.hacker_id,
       c.name,
       sum(coalesce(ss.total_submissions, 0)),
       sum(coalesce(ss.total_accepted_submissions, 0)),
       sum(coalesce(vs.total_views, 0)),
       sum(coalesce(vs.total_unique_views, 0))
from contests c
join colleges col on c.contest_id = col.contest_id
join challenges ch on col.college_id = ch.college_id

left join (
    select challenge_id,
           sum(total_submissions) as total_submissions,
           sum(total_accepted_submissions) as total_accepted_submissions
    from submission_stats
    group by challenge_id
) ss on ch.challenge_id = ss.challenge_id

left join (
    select challenge_id,
           sum(total_views) as total_views,
           sum(total_unique_views) as total_unique_views
    from view_stats
    group by challenge_id
) vs on ch.challenge_id = vs.challenge_id
group by c.contest_id, c.hacker_id, c.name

having (
    sum(coalesce(ss.total_submissions, 0)) +
    sum(coalesce(ss.total_accepted_submissions, 0)) +
    sum(coalesce(vs.total_views, 0)) +
    sum(coalesce(vs.total_unique_views))
) > 0
order by c.contest_id asc;
