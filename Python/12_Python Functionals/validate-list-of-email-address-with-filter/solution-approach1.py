# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
# Problem     Validating Email Addresses With a Filter 
# Difficulty  Medium
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 11:05 p.m.
# ──────────────────────────────────────────────────

import re

def fun(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, s))
    
