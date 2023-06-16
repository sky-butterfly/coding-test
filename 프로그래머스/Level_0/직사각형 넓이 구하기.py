def solution(dots):
    answer = 0
    x1 = dots[0][0]
    x2 = 0
    y1 = dots[0][1]
    y2 = 0
    
    for d in dots:
        x = d[0]
        y = d[1]
        
        if x != x1 :
            x2 = x
        
        if y != y1 :
            y2 = y
            
    w = 0
    h = 0
    
    if x1 > x2 :
        w = x1 - x2
    else :
        w = x2 - x1
    
    if y1 > y2 :
        h = y1 - y2
    else :
        h = y2 - y1
    
    return w * h