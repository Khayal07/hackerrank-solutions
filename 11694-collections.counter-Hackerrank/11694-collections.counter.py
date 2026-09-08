from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    
    inventory = Counter(shoe_sizes) 
    
    N = int(input())
    total_earned = 0
    
    for _ in range(N):
        size, price = map(int, input().split())
        
        if inventory[size] > 0:
            total_earned += price
            inventory[size] -= 1
            
    print(total_earned)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna