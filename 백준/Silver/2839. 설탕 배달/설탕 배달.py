import sys

n = int(sys.stdin.readline().strip())

five = n // 5

while five >= 0:
    rest = n - 5 * five
    if rest % 3 == 0:
        three = rest // 3
        print(five + three)
        break
    five -= 1
else:
    print(-1)