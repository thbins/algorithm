import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sx, sy):
    q = deque([(sx, sy)])      
    paper[sx][sy] = 0          
    area = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                paper[nx][ny] = 0
                q.append((nx, ny))
                area += 1
    return area

count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)