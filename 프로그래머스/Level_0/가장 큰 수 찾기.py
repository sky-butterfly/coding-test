def solution(array):
    answer = []
    maxvalue = array[0]
    maxindex = 0
    
    for i, a in enumerate(array):
        if maxvalue < a:
            maxvalue = a
            maxindex = i
    
    answer.append(maxvalue)
    answer.append(maxindex)
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges