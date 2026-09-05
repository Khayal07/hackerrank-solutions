if __name__ == '__main__':
    n, m = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    happiness = 0
    
    for x in arr:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
    
    print(happiness)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna