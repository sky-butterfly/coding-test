def solution(X, Y):
    arr = []
    
    for i in range(10):
        x_cnt = len(X) - len(X.replace(str(i), ''))
        y_cnt = len(Y) - len(Y.replace(str(i), ''))
        
        if x_cnt == 0 and y_cnt == 0:
            continue
        
        cnt = min(x_cnt, y_cnt)
        for c in range(cnt):
            arr.append(str(i))
            
    if len(arr) < 1:
        return '-1'
    
    arr.sort(reverse=True)
    if arr[0] == '0':
        return '0'
    
    return ''.join(arr)