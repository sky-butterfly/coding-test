def solution(a, b):
    aSum = int(str(a) + str(b))
    bSum = int(str(b) + str(a))
    
    if aSum > bSum:
        return aSum
    
    return bSum
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges