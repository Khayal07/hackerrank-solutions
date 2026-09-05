if __name__ == '__main__':  
    n = int(input())
    english_set = set(map(int, input().split()))
    
    b = int(input())
    french_set = set(map(int, input().split()))
    
    print(len(english_set | french_set))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna