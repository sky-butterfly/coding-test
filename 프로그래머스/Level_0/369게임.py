def solution(order):
    answer = 0
    
    for o in str(order):
        if '3' in o or '6' in o or '9' in o :
            answer += ( len(o) - len(o.replace('3', '')) )
            answer += ( len(o) - len(o.replace('6', '')) )
            answer += ( len(o) - len(o.replace('9', '')) )
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges