if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            a, b = input().split()
            print(int(a) // int(b))
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna