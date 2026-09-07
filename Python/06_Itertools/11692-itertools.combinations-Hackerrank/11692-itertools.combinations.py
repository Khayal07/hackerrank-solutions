from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    
    for i in range(1, k + 1):
        for j in combinations(sorted(S), i):
            print(''.join(j))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna