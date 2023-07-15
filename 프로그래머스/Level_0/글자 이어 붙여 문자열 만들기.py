def solution(my_string, index_list):
    answer = ''
    
    for i in index_list :
        answer += my_string[i]
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges