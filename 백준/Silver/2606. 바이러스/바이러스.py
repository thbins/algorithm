import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start_v):
    visited = []
    queue = deque()
    queue.append(start_v)
    visited.append(start_v)
    
    while queue:
        cur_v = queue.popleft()
       
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
                
    return visited

visited = bfs(1)

count = len(visited)

print(len(visited)-1)