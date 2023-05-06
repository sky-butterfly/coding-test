def solution(my_strings, parts):
    answer = ''
    
    for i, p in enumerate(parts) :
        start = p[0]
        end = p[1]+1
        answer += my_strings[i][start:end]
    
    return answer