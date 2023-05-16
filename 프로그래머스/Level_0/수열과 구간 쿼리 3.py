def solution(arr, queries):
    
    for q in queries:
        i = q[0]
        j = q[1]
        
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    
    return arr
