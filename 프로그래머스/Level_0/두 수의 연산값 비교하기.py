def solution(a, b):
    x = str(a) + str(b)
    y = 2 * a * b
    
    if int(x) >= y :
        return int(x)
    
    return y
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
