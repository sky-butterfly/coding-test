from collections import deque

def solution(topping):
    answer = 0
    obj = {}
    
    for t in topping:
        obj[t] = obj.get(t, 0)
        obj[t] += 1
    
    set_t = set()
    
    for t in topping:
        
        set_t.add(t)
            
        obj[t] -= 1
        if obj[t] == 0:
            del obj[t]
        
        if len(set_t) > len(obj.keys()):
            break
        
        if len(set_t) == len(obj.keys()):
            answer += 1
    
    return answer