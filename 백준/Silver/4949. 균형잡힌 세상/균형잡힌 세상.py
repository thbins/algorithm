import sys

while True:
    line = sys.stdin.readline().rstrip('\n')

    if line == '.':
        break

    stack = []
    is_balanced = True

    for ch in line:
        if ch == '(' or ch == '[':
            stack.append(ch)

        elif ch == ')':
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            stack.pop()

        elif ch == ']':
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            stack.pop()

    if is_balanced and not stack:
        print("yes")
    else:
        print("no")