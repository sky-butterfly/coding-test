def solution(date1, date2):
    answer = 0
    
    if date1[0] < date2[0]:
        return 1
    
    if date1[0] == date2[0] :
        if date1[1] < date2[1]:
            return 1
        if date1[1] == date2[1] and date1[2] < date2[2]:
            return 1
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges