def solution(array):
    answer = 0
    
    for a in array:
        s = str(a)
        n = len(s) - len(s.replace('7', ''))
        answer += n
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges