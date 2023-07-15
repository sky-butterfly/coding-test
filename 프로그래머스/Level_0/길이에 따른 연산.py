def solution(num_list):
    answer = 0
    
    if len(num_list) >= 11:
        for n in num_list:
            answer += n
        return answer
    
    answer = 1
    
    for n in num_list:
        answer *= n
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges