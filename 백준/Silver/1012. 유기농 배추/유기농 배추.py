import sys
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start_y, start_x, graph, visited, N, M):
    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = True
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    
input = sys.stdin.readline

T = int(input())

# 배추밭의 가로길이 M
# 배추밭의 세로길이 N
# 배추가 심어져 있는 위치의 개수 K

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j, graph, visited, N, M)
                count += 1
    
    print(count)