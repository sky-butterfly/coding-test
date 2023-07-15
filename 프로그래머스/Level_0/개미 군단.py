def solution(hp):
    answer = 0
    
    if hp == 0 :
        return answer
    
    x = int(hp/5)
    answer += x
    hp -= (x * 5)
    
    if hp < 1:
        return answer
    
    x = int(hp/3)
    answer += x
    hp -= (x * 3)
    if hp < 1:
        return answer
    
    answer += hp
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges