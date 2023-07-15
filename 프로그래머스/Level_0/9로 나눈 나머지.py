def solution(number):
    
    sum = 0
    
    for n in number:
        sum += int(n)
    
    return sum%9
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges