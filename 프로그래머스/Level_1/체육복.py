def solution(n, lost, reserve):    
    lost.sort()
    reserve.sort()
    
    temp_reserve = [i for i in reserve if i not in lost]
    temp_lost = [i for i in lost if i not in reserve]
    
    for r in temp_reserve:
        if r-1 in temp_lost:
            temp_lost.remove(r-1)
            continue
        if r+1 in temp_lost:
            temp_lost.remove(r+1)
            continue
    
    return n- len(temp_lost)