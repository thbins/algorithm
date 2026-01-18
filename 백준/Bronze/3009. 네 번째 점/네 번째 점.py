import sys
from collections import Counter

xs = []
ys = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)

cx = Counter(xs)
cy = Counter(ys)

ans_x = next(k for k, v in cx.items() if v == 1)
ans_y = next(k for k, v in cy.items() if v == 1)

print(ans_x, ans_y)