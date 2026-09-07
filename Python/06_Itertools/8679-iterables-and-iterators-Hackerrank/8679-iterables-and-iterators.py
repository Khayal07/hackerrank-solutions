from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    letters = input().split()
    K = int(input())
    
    all_combinations = list(combinations(letters, K))
    
    a_combinations = [comb for comb in all_combinations if 'a' in comb]
    
    probability = len(a_combinations) / len(all_combinations)
    
    print(probability)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna