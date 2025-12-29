import sys

input = sys.stdin.readline

N, M = map(int, input().split())
prices = [int(input()) for _ in range(M)]
prices.sort()

best_price = 0
best_revenue = 0

for i, p in enumerate(prices):
    buyers = M - i
    sold = min(N, buyers)
    revenue = p * sold
    if revenue > best_revenue:
        best_revenue = revenue
        best_price = p

print(best_price, best_revenue)