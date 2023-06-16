def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        num = 0
        
        for k in range(2, (i//2)+1):
            if i%k == 0:
                answer += 1
                break;
    
    return answer