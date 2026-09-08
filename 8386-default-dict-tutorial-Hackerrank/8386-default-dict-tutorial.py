from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    d = defaultdict(list)
    
    
    for i in range(1, n + 1):
        word = input().strip()
        d[word].append(i)
        
    for _ in range(m):
        word = input().strip()
        if word in d:
            print(*d[word])
        else:
            print(-1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna