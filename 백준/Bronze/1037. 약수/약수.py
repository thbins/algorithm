import sys
input = sys.stdin.readline

k = int(input().strip())
arr = list(map(int, input().split()))

arr.sort()
print(arr[0] * arr[-1])