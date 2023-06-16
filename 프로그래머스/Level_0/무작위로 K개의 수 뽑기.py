def solution(arr, k):
    answer = []
    
    for a in arr:
        if len(answer) == k:
            break
        
        if (a in answer) == False:
            answer.append(a)
            
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    
    return answer