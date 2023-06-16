def solution(str_list):
    answer = []
    
    if ('l' in str_list) == False and ('r' in str_list) == False:
        return answer
    
    for i, s in enumerate(str_list):
        if s == 'l':
            answer.extend(str_list[:i])
            break
        if s == 'r':
            if i < len(str_list)-1:
                answer.extend(str_list[i+1:])
            break
    
    return answer