import sys

input = sys.stdin.readline

N, B = input().split()
B = int(B)

answer = 0

for ch in N:
    if '0' <= ch <= '9':
        value = ord(ch) - ord('0')
    else:
        value = ord(ch) - ord('A') + 10
        
    answer = B * answer + value
    
print(answer)