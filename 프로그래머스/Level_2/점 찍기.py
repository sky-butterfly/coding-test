def solution(k, d):
    
    answer = 0
    
    x = d - (d%k)
    while x > -1:
        
        y = int((d**2 - x**2)**0.5)
        answer += (y//k + 1)
        
        x -= k
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges