if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_arr = list(set(arr))
    sorted_unique_arr = sorted(unique_arr)
    print(sorted_unique_arr[-2])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna