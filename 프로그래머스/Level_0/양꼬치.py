def solution(n, k):
    answer = 0
    
    k -= (int(n/10))
    
    answer += (n * 12000)
    answer += (k * 2000)
    
    return answer
