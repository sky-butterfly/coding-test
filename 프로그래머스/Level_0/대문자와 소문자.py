def solution(my_string):
    answer = ''
    
    for str in my_string:
        if str.isupper():
            answer += str.lower()
            continue
        answer += str.upper()
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges