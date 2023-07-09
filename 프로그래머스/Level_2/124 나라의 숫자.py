def solution(n):
    answer = ''
    obj = {0: 1, 1:2, 2:4}
    size = 1
    c = n
    
    while c > 3:
        c = c//3
        size += 1
    
    diff = 0
    for i in range(1, size+1):
        count = 3**i
        m = (n-diff)%count
        if m == 0:
            m = count
        k = 3**(i-1)
        
        nn = m//k
        if m%k == 0:
            nn -= 1
        answer = str(obj[nn]) + answer
            
        diff += count
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges