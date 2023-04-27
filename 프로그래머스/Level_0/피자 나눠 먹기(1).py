def solution(n):
    answer = 0
    
    answer += (int(n/7))
    if(n%7 > 0):
        answer += 1
    
    return answer
    