import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    
    day_index = calendar.weekday(year, month, day)
    
    print(calendar.day_name[day_index].upper())


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna