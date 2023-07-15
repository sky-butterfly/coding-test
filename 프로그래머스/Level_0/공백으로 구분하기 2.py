def solution(my_string):
    answer = []
    
    for m in my_string.split(' '):
        if m:
            answer.append(m)
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges