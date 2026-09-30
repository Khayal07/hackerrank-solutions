# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true
# Problem     Array Manipulation
# Difficulty  Hard
# Subdomain   Arrays
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-30, 10:26 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = [0] * (n + 2)
    
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
        
    max_val = 0
    current = 0
    
    for val in arr:
        current += val
        if current > max_val:
            max_val = current
            
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
