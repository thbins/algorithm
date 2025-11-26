import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    stack = []
    is_vps = True
    
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else: # ch == ')'
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    
    # 문자열을 다 돈 뒤에도 스택에 괄호가 남아있으면 NO
    if stack:
        is_vps = False
        
    print('YES' if is_vps else 'NO')  
   
'''
# 스택이 아닌 count 변수의 연산을 통해 푸는 풀이도 있다.

import sys

input = sys.stdin.readline

T = int(input())  

for _ in range(T):
    s = input().strip()  
    cnt = 0
    is_vps = True

    for ch in s:
        if ch == '(':
            cnt += 1
        else:  # ch == ')'
            cnt -= 1

        # 중간에 닫는 괄호가 더 많아지면 이미 틀림
        if cnt < 0:
            is_vps = False
            break

    if cnt != 0:
        is_vps = False

    print("YES" if is_vps else "NO")
'''