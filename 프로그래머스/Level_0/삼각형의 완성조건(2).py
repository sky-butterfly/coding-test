def solution(sides):
    answer = 0
    
    mi = min(sides[0], sides[1])
    ma = max(sides[0], sides[1])
    
    answer += mi
    answer += (mi-1)
    
    return answer