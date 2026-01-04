import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def count_regions(board):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            cnt += 1
            color = board[i][j]
            q = deque([(i, j)])
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if not visited[nx][ny] and board[nx][ny] == color:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt

# 일반인
normal = count_regions(grid)

# 적록색약: G를 R로 변환해서 동일 처리
blind_grid = [row[:] for row in grid]
for i in range(N):
    for j in range(N):
        if blind_grid[i][j] == 'G':
            blind_grid[i][j] = 'R'

blind = count_regions(blind_grid)

print(normal, blind)