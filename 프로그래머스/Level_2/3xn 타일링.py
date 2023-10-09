from itertools import permutations, product, combinations

def solution(n):
    answer = 8
    obj = {2 : 3}
    
    if n == 2:
        return obj[n] % 1000000007
    
    i = 4
    while i < n :
        
        s = 2
        k = 2
        while k < i:
            s += obj[k]*2            
            k += 2
            
        obj[i] = s + obj[i-2]
        answer += obj[i]*2
        i += 2
    
    answer += obj[n-2]
    
    return answer % 1000000007
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges