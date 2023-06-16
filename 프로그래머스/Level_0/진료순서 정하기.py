def solution(emergency):
    answer = []
    obj = {}
        
    tmp = sorted(emergency, reverse=True)
    
    for i in range(1, len(tmp)+1):
        obj[tmp[i-1]] = i
        
    for e in emergency:
        answer.append(obj[e])
    
    return answer