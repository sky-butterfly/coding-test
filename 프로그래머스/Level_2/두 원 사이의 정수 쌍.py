import math

def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2+1):        
        mx = math.floor(((r2**2) - (i**2))**0.5)
        mn = 0
        if r1 >= i:
            mn = math.ceil(((r1**2) - (i**2))**0.5)
        
        answer += (mx - mn + 1) 
    
    return answer * 4

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges