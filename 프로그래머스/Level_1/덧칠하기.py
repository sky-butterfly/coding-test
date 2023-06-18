import math

def solution(n, m, section):
    answer = 0
    arr = []
    
    start = section[0]
    end = section[len(section)-1]
    
    while len(section) > 0:            
        s = section[0]
        if s+(m-1) > n:
            answer += 1
            break
        
        for k in range(m):
            ss = section[0]
            if ss >= s+m:
                break
            section.pop(0)
            if len(section) < 1:
                break
        
        answer += 1
    
    return answer