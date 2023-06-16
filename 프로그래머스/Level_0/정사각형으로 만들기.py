def solution(arr):
    
    row = len(arr)
    column = len(arr[0])
    diff = abs(row-column)
    
    if row > column :
        for i, a in enumerate(arr):
            
            for k in range(diff):
                a.append(0)
                arr[i] = a
        
    else:
        for i in range(diff):
            add = []
            
            for c in range(column):
                add.append(0)
            
            arr.append(add)
        
    
    return arr