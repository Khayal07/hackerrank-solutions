from collections import deque

def check_piling():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        d = deque(map(int, input().split()))
        
        last_placed = float('inf')
        possible = True
        
        while d:
            if d[0] >= d[-1]:
                chosen = d.popleft()
            else:
                chosen = d.pop()
                
            if chosen > last_placed:
                possible = False
                break
                
            last_placed = chosen
        
        print("Yes" if possible else "No")

if __name__ == '__main__':
    check_piling()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna