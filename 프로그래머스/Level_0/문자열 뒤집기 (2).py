def solution(my_string, s, e):
    middle_list = list(my_string[s:e+1])
    middle_list.reverse()
    middle = ''.join(middle_list)
    
    answer = ''
    answer += my_string[:s]
    answer += middle
    answer += my_string[e+1:]
    
    return answer