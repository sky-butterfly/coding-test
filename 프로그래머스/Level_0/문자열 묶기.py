def solution(strArr):
    answer = 0
    obj = {}
    
    for s in strArr:
        size = len(s)
        if len(obj) < 1:
            obj[size] = 1
            continue
        if size in obj.keys():
            obj[size] = (obj[size] + 1)
            continue
        obj[size] = 1
    
    for o in obj.keys():
        if answer < obj[o]:
            answer = obj[o]
    
    return answer