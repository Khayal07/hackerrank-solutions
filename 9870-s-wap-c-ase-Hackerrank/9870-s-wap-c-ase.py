def swap_case(s):
    a = ""
    for i in s:
        if i == i.lower():
            a = a + i.upper()
        else:
            a = a + i.lower()
    return a



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna