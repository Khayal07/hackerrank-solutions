if __name__ == '__main__':
    _ = input()
    A = set(map(int, input().split()))
    
    N = int(input())
    
    for _ in range(N):
        cmd = input().split()
        op_name = cmd[0]
        other_set = set(map(int, input().split()))
        
        getattr(A, op_name)(other_set)
    
    print(sum(A))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna