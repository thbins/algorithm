import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start_y, start_x):
    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = True
    count = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    count += 1
                    
    return count

sizes = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            size = bfs(i, j)
            sizes.append(size)
            
sizes.sort()

print(len(sizes))
for s in sizes:
    print(s)