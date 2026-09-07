import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    
    angle_rad = math.atan2(AB, BC)
    angle_deg = round(math.degrees(angle_rad))
    
    print(f"{angle_deg}{chr(176)}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna