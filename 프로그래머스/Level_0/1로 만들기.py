def solution(num_list):
    answer = 0
    
    for n in num_list:
        while(n > 1):
            answer += 1
            
            if n%2 == 0:
                n /= 2
            else :
                n -= 1
                n /= 2
    
    return answer