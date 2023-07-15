def solution(names):
    answer = []
    size = int(len(names)/5)
    
    answer.append(names[0])
    for s in range(1, size) :
        answer.append(names[5*s])
        
    if len(names)%5 > 0 :
        answer.append(names[5*size])
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges