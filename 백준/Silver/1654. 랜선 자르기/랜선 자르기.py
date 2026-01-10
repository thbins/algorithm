import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

lo, hi = 1, max(lines)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2 

    cnt = 0
    for x in lines:
        cnt += x // mid

    if cnt >= N:
        ans = mid         
        lo = mid + 1      
    else:
        hi = mid - 1       

print(ans)