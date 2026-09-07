from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())
    
    lists = [list(map(int, input().split()))[1:] for _ in range(K)]
    
    max_value = max(sum(x**2 for x in comb) % M for comb in product(*lists))
    
    print(max_value)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna