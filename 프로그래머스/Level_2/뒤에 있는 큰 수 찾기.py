from collections import deque

def solution(numbers):
    answer = [-1]*len(numbers)
    stack = deque()
    
    for i in range(len(numbers)):
        
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges