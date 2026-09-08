from collections import OrderedDict

if __name__ == '__main__':
    N = int(input())
    ordered_dictionary = OrderedDict()
    
    for _ in range(N):
        item_name, price = input().rsplit(' ', 1)
        price = int(price)
        
        ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + price
        
    for item_name, net_price in ordered_dictionary.items():
        print(item_name, net_price)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna