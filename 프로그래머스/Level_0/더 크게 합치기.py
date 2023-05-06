def solution(a, b):
    aSum = int(str(a) + str(b))
    bSum = int(str(b) + str(a))
    
    if aSum > bSum:
        return aSum
    
    return bSum