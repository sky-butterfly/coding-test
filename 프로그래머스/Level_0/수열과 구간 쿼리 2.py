def solution(arr, queries):
    answer = []
    
    for q in queries:
        s = q[0]
        e = q[1]
        k = q[2]
        
        min = -1
        for i in range(s, e+1):
            if arr[i] <= k:
                continue
            if min == -1 or min > arr[i]:
                min = arr[i]
        
        answer.append(min)
            
    return answer
