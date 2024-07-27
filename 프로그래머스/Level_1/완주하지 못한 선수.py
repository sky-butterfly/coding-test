def solution(participant, completion):
    answer = ''
    
    obj = {}
    
    for p in participant:
        obj[p] = obj.get(p, 0) + 1
        
    for c in completion:
        if obj.get(c, -1) == -1:
            return c
        obj[c] = obj[c] - 1
    
    for key in obj.keys():
        if obj[key] == 1:
            answer = key
            break
    

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges