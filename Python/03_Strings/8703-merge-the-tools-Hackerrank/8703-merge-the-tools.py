def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i : i + k]
        print("".join(dict.fromkeys(part)))



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna