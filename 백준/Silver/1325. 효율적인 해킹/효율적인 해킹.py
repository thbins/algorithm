import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    
visited = [0] * (N+1)
token = 0

def bfs(start_v):
    global token
    queue = deque([start_v])
    token += 1
    visited[start_v] = token
    cnt = 1
    
    while queue:
        cur_v = queue.popleft()
        
        for nxt in graph[cur_v]:
            if visited[nxt] != token:
                visited[nxt] = token
                cnt += 1
                queue.append(nxt)
                
    return cnt

counts = [0] * (N + 1)
mx = 0

for i in range(1, N + 1):
    c = bfs(i)
    counts[i] = c
    if c > mx : mx = c
    
ans = [str(i) for i in range(1, N + 1) if counts[i] == mx]
print(" ".join(ans))