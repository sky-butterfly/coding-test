def solution(my_string, indices):
    answer = ''
    
    for i, s in enumerate(my_string):
        if (i in indices) == False:
            answer += s
    
    return answer