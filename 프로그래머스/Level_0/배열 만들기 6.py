def solution(arr):
    answer = []
    i = 0
    
    while i < len(arr):
        if len(answer) < 1:
            answer.append(arr[i])
            i += 1
            continue
        if answer[len(answer)-1] == arr[i] :
            answer.pop()
            i += 1
            continue
        answer.append(arr[i])
        i += 1
    
    if len(answer) < 1:
        answer.append(-1)
    
    return answer