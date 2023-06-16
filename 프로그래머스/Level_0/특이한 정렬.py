
def solution(numlist, n):
    answer = []
    obj = {}
    
    for num in numlist :
        key = abs(n-num)
        if key in obj.keys():
            arr = obj[key]
            arr.append(num)
            obj[key] = arr
            continue
        obj[key] = [num]
    
    keys = sorted(obj)
    
    for k in keys:
        arr = obj[k]
        arr.sort(reverse=True)
        answer.extend(arr)
    
    return answer