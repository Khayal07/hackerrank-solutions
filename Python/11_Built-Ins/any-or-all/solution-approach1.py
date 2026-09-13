# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Problem     Any or All
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 01:59 a.m.
# ──────────────────────────────────────────────────

_, arr = input(), input().split()
print(all(int(x) > 0 for x in arr) and any(x == x[::-1] for x in arr))
