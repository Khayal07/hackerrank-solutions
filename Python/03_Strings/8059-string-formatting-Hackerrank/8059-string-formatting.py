def print_formatted(number):
    
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        dec_val = f"{i:{width}d}"
        oct_val = f"{i:{width}o}"
        hex_val = f"{i:{width}X}"
        bin_val = f"{i:{width}b}"
        
        print(f"{dec_val} {oct_val} {hex_val} {bin_val}")
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna