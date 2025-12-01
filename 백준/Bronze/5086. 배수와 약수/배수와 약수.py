import sys

input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    if b % a == 0:
        print("factor")      # a는 b의 약수
    elif a % b == 0:
        print("multiple")    # a는 b의 배수
    else:
        print("neither")     # 둘 다 아님