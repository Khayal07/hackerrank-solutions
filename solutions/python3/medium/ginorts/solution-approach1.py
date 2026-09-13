# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
# Problem     ginortS
# Difficulty  Medium
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 02:00 a.m.
# ──────────────────────────────────────────────────

print(*sorted(input(), key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper(), c)), sep='')
