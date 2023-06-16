def solution(my_string):
    answer = []
    
    for m in my_string.split(' '):
        if m:
            answer.append(m)
    
    return answer