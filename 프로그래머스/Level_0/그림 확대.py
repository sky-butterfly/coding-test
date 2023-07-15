def solution(picture, k):
    answer = []
    
    for p in picture:
        s = ''
        for pp in p:
            for i in range(k):
                s += pp
        
        for i in range(k):
            answer.append(s)
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges