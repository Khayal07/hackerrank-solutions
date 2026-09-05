if __name__ == '__main__':
    K = int(input())
    rooms = list(map(int, input().split()))
    
    captain_room = (K * sum(set(rooms)) - sum(rooms)) // (K - 1)
    
    print(captain_room)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna