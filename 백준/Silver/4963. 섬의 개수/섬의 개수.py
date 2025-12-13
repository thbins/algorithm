import sys
from collections import deque

input = sys.stdin.readline

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc))
        visited[sr][sc] = True

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    if not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)