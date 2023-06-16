def solution(a, b, c, d):
    answer = 0
    
    if a == b and b == c and c == d :
        return 1111 * a
    
    arr = [a, b, c, d]
    obj = {}
    
    for a in arr:
        if a in obj.keys():
            obj[a] = obj[a]+1
        else:
            obj[a] = 1
    
    p = 0
    q = 0
    r = 0
    
    keys = sorted(obj)
    
    if len(keys) == 2:
        if obj[keys[0]] == 3:
            
            p = keys[0]
            q = keys[1]
            
            return (10 * p + q) ** 2
        
        if obj[keys[1]] == 3:
            p = keys[1]
            q = keys[0]
            
            return (10 * p + q) ** 2
        
        if obj[keys[0]] == 2:
            
            p = keys[0]
            q = keys[1]
            
            return (p + q) * abs(p - q)
        
    if len(keys) == 3:
        
        for i, k in enumerate(keys):
            if obj[k] == 2:
                keys.remove(k)
                q = keys[0]
                r = keys[1]
                
                return q * r
    
    if len(keys) == 4:
        return keys[0]
    
    return answer