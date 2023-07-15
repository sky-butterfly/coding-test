def solution(rsp):
    answer = ''
    
    for r in rsp :
        if r == '2' :
            answer += '0'
            continue
        elif r == '0' :
            answer += '5'
            continue
        answer += '2'
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges