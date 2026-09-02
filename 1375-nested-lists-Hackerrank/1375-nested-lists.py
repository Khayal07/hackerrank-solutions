if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores = sorted(set([score for name, score in records]))
        
    second_lowest = scores[1]
        
    names = [name for name, score in records if score == second_lowest]
        
    for name in sorted(names):
        print(name)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna