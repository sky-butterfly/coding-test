def solution(arr):
    stk = []
    
    i = 0
    while(i < len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
            continue
        if stk[len(stk)-1] < arr[i]:
            stk.append(arr[i])
            i += 1
            continue
        del stk[len(stk)-1]
    
    
    return stk
