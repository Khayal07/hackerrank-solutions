if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        _ = input()
        A = set(map(int, input().split()))
        _ = input()
        B = set(map(int, input().split()))
        
        print(A.issubset(B))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna