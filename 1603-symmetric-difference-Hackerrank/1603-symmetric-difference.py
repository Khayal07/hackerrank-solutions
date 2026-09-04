if __name__ == '__main__':
    M = int(input())
    set_a = set(map(int, input().split()))
    
    N = int(input())
    set_b = set(map(int, input().split()))
    
    intersection = set_a.intersection(set_b)
    
    for i in intersection:
        set_a.remove(i)
        set_b.remove(i)
        
    new_set = set_a.union(set_b)
    
    for j in sorted(new_set):
        print(j)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna