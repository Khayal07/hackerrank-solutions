# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
# Problem     Map and Lambda Function
# Difficulty  Easy
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 11:02 p.m.
# ──────────────────────────────────────────────────

cube = lambda x: x ** 3 

def fibonacci(n):
    lis = [0, 1]
    for i in range(2, n):
        lis.append(lis[i - 1] + lis[i - 2])
    return lis[:n]

