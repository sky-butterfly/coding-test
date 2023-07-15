def solution(numbers, k):
    answer = 0
    size = len(numbers)
    num = 0
    
    for i in range(1, k):
        num += 2
        answer = num%size + 1
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges