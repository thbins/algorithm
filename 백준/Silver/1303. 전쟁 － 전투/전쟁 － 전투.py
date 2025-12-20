import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())   
grid = [list(input().strip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sy, sx):
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    team = grid[sy][sx]
    cnt = 1

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                if grid[ny][nx] == team:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1
    return team, cnt

w_power = 0
b_power = 0

for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            team, cnt = bfs(y, x)
            if team == 'W':
                w_power += cnt * cnt
            elif team == 'B':
                b_power += cnt * cnt

print(w_power, b_power)