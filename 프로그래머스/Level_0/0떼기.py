def solution(n_str):
    
    for n in n_str :
        if n.startswith('0'):
            n_str = n_str[1:]
        else :
            return n_str
    
    return n_str
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges