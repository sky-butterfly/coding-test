from itertools import permutations

def solution(numbers):
    answer = ''
    
    str_arr = list(map(str, numbers))
    str_arr.sort(key=lambda x: (x*4)[:4], reverse=True)
    
    answer = ''.join(str_arr)
    
    if answer[0] == '0':
        return '0'
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges