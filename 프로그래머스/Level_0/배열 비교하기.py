def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            return 1
        return -1
    
    sum1 = 0
    sum2 = 0
    for a in arr1:
        sum1 += a
    
    for a in arr2:
        sum2 += a
    
    if sum1 > sum2 :
        return 1
    if sum2 > sum1 :
        return -1
    
    return 0