def solution(my_string, m, c):
    answer = ''
    
    for i in range(int(len(my_string)/m)):
        answer += my_string[i*m+(c-1)]
    
    return answer