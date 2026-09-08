from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    
    for _ in range(n):
        cmd = input().split()
        method = cmd[0]
        args = cmd[1:]
        
        getattr(d, method)(*args)
        
    print(*d)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna