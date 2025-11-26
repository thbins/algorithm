import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
sorted_unique = sorted(set(arr))

compress = {value: idx for idx, value in enumerate(sorted_unique)}

ans = []
for x in arr:
    ans.append(str(compress[x]))

print(' '.join(ans))