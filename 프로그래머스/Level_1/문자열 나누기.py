def solution(s):
    answer = 0
    
    first = s[0]
    x = 1
    y = 0
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)):
        
        ss = s[i]
        
        if x == y:
            answer += 1
            first = ss
            x = 0
            y = 0
            
        if i == len(s)-1:
            answer += 1    
            break
            
        if first == ss:
            x += 1
        else:
            y += 1  
    
    return answer