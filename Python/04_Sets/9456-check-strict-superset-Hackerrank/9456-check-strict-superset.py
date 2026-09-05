if __name__ == '__main__':
    
    A = set(map(int, input().split()))
    
    N = int(input())
    
    is_strict_superset = all(A > set(map(int, input().split()))for _ in range(N))
    
    print(is_strict_superset)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna