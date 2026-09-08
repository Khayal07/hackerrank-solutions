#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    counts = Counter(s)
    
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_counts[:3]:
        print(char, count)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna