N = int(input())

start = max(0, N - 9 * len(str(N)))
answer = 0

for x in range(start, N + 1):
    s = x + sum(map(int, str(x)))
    if s == N:
        answer = x
        break

print(answer)