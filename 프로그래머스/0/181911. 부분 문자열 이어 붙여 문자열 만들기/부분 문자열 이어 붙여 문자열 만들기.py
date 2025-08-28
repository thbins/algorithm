def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(parts)):
        current_parts = parts[i]
        current_strings = my_strings[i]
        answer +=  current_strings[current_parts[0]:current_parts[1]+1]
        
    return answer