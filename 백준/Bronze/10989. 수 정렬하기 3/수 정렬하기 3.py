import sys

input = sys.stdin.readline

N = int(input())
counts = [0] * 10001  

for _ in range(N):
    counts[int(input())] += 1

for i in range(1, 10001):
    c = counts[i]
    if c:
        for _ in range(c):
            print(i)