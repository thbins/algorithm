import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
papers = list(map(int, input().split()))

ballons = deque(range(1, N + 1)) 
ans = []

while ballons:
    i = ballons.popleft()
    ans.append(i)
    
    n = papers[i - 1]
    
    if not ballons:
        break

    if n > 0:
        ballons.rotate(-(n - 1))
    else:  # n < 0
        ballons.rotate(-n)

print(*ans)