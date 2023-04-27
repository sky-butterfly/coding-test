def solution(n):
    answer = 2
    
    m = n ** 0.5
    
    if m%1 == 0:
        answer = 1
    
    return answer