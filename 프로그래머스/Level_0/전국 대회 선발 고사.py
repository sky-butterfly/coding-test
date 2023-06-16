def solution(rank, attendance):
    obj = {}
    
    for i, r in enumerate(rank):
        if attendance[i]:
            obj[r] = i
    
    keys = sorted(obj)    
    
    a = obj[keys[0]]
    b = obj[keys[1]]
    c = obj[keys[2]]
    
    return (10000*a) + (100*b) + c