import sys

input = sys.stdin.readline

N = int(input())

paper = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(y, y + 10):      # 세로 
        for j in range(x, x + 10):  # 가로
            paper[i][j] = 1   

area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

print(area)