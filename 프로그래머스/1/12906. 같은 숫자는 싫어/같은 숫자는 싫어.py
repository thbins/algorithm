def solution(arr):
    pre_value = 10
    answer = []
    
    for i in arr:
        if i != pre_value:
            answer.append(i)
        pre_value = i
        
    return answer