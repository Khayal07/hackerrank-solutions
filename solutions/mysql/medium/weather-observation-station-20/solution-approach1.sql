-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
-- Problem     Weather Observation Station 20
-- Difficulty  Medium
-- Subdomain   Aggregation
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-09-21, 01:58 a.m.
-- ──────────────────────────────────────────────────

with ranked_stations as (
    select lat_n, row_number() over (order by lat_n) as rn, count(*) over () as total_rows
    from station
)
select round(lat_n, 4)
from ranked_stations
where rn = ceil(total_rows / 2);
