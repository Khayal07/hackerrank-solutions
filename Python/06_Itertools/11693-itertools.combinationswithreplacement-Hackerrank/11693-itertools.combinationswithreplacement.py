from itertools import combinations_with_replacement

if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    
    for i in combinations_with_replacement(sorted(S), k):
        print(''.join(i))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna