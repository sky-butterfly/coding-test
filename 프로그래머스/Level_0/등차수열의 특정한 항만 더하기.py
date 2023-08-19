def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        x = a + (i*d)
        
        if included[i] == True :
            answer += x
            
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
