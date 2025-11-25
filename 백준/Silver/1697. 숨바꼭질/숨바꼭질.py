import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100000
dist = [-1] * (MAX +1)

def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    dist[start_v] = 0
    
    while queue:
        x = queue.popleft()
        
        if x == K:
            return dist[x]
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and dist[nx] == -1:
                dist[nx] = dist[x]+1
                queue.append(nx)
               
    return -1

print(bfs(N))