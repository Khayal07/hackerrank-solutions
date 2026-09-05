if __name__ == '__main__':
    n = int(input())
    eng_set = set(map(int, input().split()))
    
    b = int(input())
    fre_set = set(map(int, input().split()))
    
    print(len(eng_set.difference(fre_set)))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna