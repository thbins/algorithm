import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = []

def dfs(depth, start):
    if depth == M:
        print(*path)
        return

    for i in range(start, N + 1):
        path.append(i)          
        dfs(depth + 1, i + 1)   
        path.pop()              

dfs(0, 1)