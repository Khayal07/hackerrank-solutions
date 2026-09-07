from itertools import groupby

if __name__ == '__main__':
    S = input()
    
    a = [(len(list(group)), int(key)) for key, group in groupby(S)]
    
    print(*a)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna