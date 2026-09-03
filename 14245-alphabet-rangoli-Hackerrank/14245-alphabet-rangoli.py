import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    lines = []
    
    for i in range(size):
        s = alphabet[i:size]
        row = '-'.join(s[::-1] + s[1:])
        lines.append(row.center(width, '-'))
        
    result = lines[::-1] + lines[1:]
    print('\n'.join(result))



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna