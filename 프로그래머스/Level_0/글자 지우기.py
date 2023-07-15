def solution(my_string, indices):
    answer = ''
    
    for i, s in enumerate(my_string):
        if (i in indices) == False:
            answer += s
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges