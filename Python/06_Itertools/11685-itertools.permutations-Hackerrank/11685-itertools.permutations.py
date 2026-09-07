from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    
    for p in permutations(sorted(S), k):
        print(''.join(p))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna