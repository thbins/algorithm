def solution(arr):
    stk = []
    for x in arr:
        if stk and stk[-1] == x:
            stk.pop()
        else:
            stk.append(x)
            
    if not stk:
        stk.append(-1
                  )
    return stk