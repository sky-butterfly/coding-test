def solution(n):
    answer = 0
    obj = {}
    
    i = 0
    while i <= n:
        if i == 0 or i == 1:
            obj[i] = 1
            i += 1
            continue
        
        obj[i] = (obj[i-1] + obj[i-2])%1000000007
        i += 1
        
    if n == 1:
        answer = 1
    else:
        answer = obj[n]
    
    return answer