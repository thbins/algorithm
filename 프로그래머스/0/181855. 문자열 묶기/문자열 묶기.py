def solution(strArr):
    count = {}
    
    for i in strArr:
        length = len(i)
        
        if length in count:
            count[length] += 1
        else:
            count[length] = 1
        
    return max(count.values())