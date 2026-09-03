# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    #up
    for i in range(1, N, 2):
        print(('.|.' * i).center(M, '-'))
        
    #center
    print('WELCOME'.center(M, '-'))
    
    #below
    for i in range(N - 2, 0, -2):
        print(('.|.' * i).center(M, '-'))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna