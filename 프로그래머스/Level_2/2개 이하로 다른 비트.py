def solution(numbers):
    answer = []
    
    for num in numbers:
        x = (num^(num+1)) >> 2
        x += num
        x += 1
        answer.append(x)
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
    
    