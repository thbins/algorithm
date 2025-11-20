import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    graph[i].sort(reverse=True)

visited = [0] * (N+1)    
order = 1

def bfs(start_v):
    global order
    queue = deque([start_v])
    visited[start_v] = order
    order += 1
    
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if visited[v] == 0:
                visited[v] = order
                order += 1
                queue.append(v)
                
bfs(R)       
         
for i in range(1, N+1):
    print(visited[i])