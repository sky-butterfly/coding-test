def solution(before, after):
    answer = 0
    
    a_arr = list(after)
    b_arr = list(before)
    
    a_arr.sort()
    b_arr.sort()
    
    a = str(''.join(a_arr))
    b = str(''.join(b_arr))
    
    if a == b:
        answer = 1
    
    return answer