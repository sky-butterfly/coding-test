def solution(array):
    obj = {}
    
    for a in array:
        if a in obj.keys():
            obj[a] = obj[a]+1
        else:
            obj[a] = 1
    
    obj2 = {}
    
    for k in obj.keys():
        num = obj[k]
        
        if num in obj2.keys():
            arr = obj2[num]
            arr.append(k)
            obj2[num] = arr
            continue
        
        obj2[num] = [k]
    
    keys = sorted(obj2)
    key = keys[len(keys)-1]
    arr2 = obj2[key]
    
    if len(arr2) > 1:
        return -1
    
    return arr2[0]