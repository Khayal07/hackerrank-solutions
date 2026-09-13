# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
# Problem     Zipped!
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 01:47 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N, X = map(int, input().split())
    
    scores = []
    for _ in range(X):
        scores.append(list(map(float, input().split())))
    

    for student_scores in zip(*scores):
        print(sum(student_scores) / X)
