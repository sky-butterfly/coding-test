def solution(arr, k):
    answer = []
    
    if k%2 == 1:
        for a in arr:
            answer.append(a*k)
        return answer
    
    for a in arr:
        answer.append(a+k)
    return answer