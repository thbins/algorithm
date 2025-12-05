import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()                 # 오름차순
B.sort(reverse=True)     # 내림차순

ans = 0
for i in range(N):
    ans += A[i] * B[i]

print(ans)