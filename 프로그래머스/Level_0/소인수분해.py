def solution(n):
    answer = []
    i = 2
    
    while(i <= n):
        if n%i == 0:
            n = int(n/i)
            if (i in answer) == False:
                answer.append(i)
        else:
            i+=1
    
    return answer