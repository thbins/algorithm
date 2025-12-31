import sys

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))

count = {}
for x in cards:
    count[x] = count.get(x, 0) + 1

M = int(input().strip())
queries = list(map(int, input().split()))

print(' '.join(str(count.get(q, 0)) for q in queries))