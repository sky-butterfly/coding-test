def solution(num, k):
    answer = -1
    
    for i, v in enumerate(str(num)):
        if int(v) == k :
            answer = i+1
            break;
    
    return answer