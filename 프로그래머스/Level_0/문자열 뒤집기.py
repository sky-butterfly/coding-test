def solution(my_string):
    answer = ''
    
    for str in reversed(my_string):
        answer+=str
    
    return answer
