import sys

input = sys.stdin.readline

N = int(input().strip())
files = [input().strip() for _ in range(N)]

pattern = list(files[0])
length = len(pattern)

for i in range(length):
    ch = files[0][i]
    for j in range(1, N):
        if files[j][i] != ch:
            pattern[i] = '?'
            break

print(''.join(pattern))