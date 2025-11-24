import sys

input = sys.stdin.readline

N = int(input())

words = set() 

for _ in range(N):
    word = input().strip()
    words.add(word)

arr = list(words)

arr.sort(key=lambda x: (len(x), x))

for i in arr:
    print(i)