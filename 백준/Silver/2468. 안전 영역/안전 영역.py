import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]

# 지도에서 최대 높이 찾기
max_height = 0
for i in range(N):
    for j in range(N):
        if height[i][j] > max_height:
            max_height = height[i][j]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx, h, visited):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < N:
                # 아직 방문 안했고, 물에 잠기지 않은 칸이면
                if not visited[ny][nx] and height[ny][nx] > h:
                    visited[ny][nx] = True
                    queue.append((ny, nx))


answer = 0

# 비가 하나도 안 올 수도 있으므로 h = 0부터 시작
for h in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            # 잠기지 않은 칸이면서 아직 방문하지 않은 곳이면 새로운 안전 영역
            if height[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited)
                cnt += 1

    # 비가 너무 많이 와서 다 잠기면 cnt가 0일 수도 있음
    if cnt > answer:
        answer = cnt

print(answer)