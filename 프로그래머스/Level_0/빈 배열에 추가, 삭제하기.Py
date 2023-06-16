def solution(arr, flag):
    answer = []
    
    for i, f in enumerate(flag):
        if f == True:
            for n in range(arr[i]*2):
                answer.append(arr[i])
            continue
        for n in range(arr[i]):
            answer.pop()
    
    return answer