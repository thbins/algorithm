import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(1, N+1):
    x, y = map(int, input().split())
    arr.append((x, y))
    
arr.sort()
    
for x, y in arr:
    print(x, y)