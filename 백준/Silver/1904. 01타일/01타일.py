import sys
input = sys.stdin.readline

n = int(input().strip())
MOD = 15746

memo = {1: 1, 2: 2}

if n <= 2:
    print(memo[n])
else:
    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % MOD
    print(memo[n])