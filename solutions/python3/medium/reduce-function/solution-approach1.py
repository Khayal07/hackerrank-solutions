# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
# Problem     Reduce Function
# Difficulty  Medium
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 11:10 p.m.
# ──────────────────────────────────────────────────



def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

