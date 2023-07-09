from itertools import permutations

def solution(numbers):
    answer = 0
    
    num_set = set()
    for i in range(1, len(numbers)+1):
        for c in permutations(numbers, i):
            cc = int(''.join(c))
            
            if cc in num_set:
                continue
                
            if get(cc):
                answer += 1
                
            num_set.add(cc)
    
    return answer

def get(n):
    
    if n == 1 or n == 0:
        return False
    
    if n == 2:
        return True
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges