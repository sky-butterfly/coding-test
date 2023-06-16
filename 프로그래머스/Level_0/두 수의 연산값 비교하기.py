def solution(a, b):
    x = str(a) + str(b)
    y = 2 * a * b
    
    if int(x) >= y :
        return int(x)
    
    return y
