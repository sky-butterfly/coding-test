def solution(arr, queries):
    
    for i, q in enumerate(queries):
        for num in range(q[0], q[1]+1):
            arr[num] += 1
    
    return arr