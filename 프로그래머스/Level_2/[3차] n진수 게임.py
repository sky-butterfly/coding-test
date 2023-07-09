def solution(n, t, m, p):
    answer = ''
    
    idx = 0
    s = []
    cnt = 0
    num = 0
    for i in range((m*t)+1):
        num += 1
        
        if len(s) == 0:
            s = list(str(getNum(idx, n)))
            idx += 1
        
        if num == p:
            if len(s) > 0:
                answer += s[0]
            cnt += 1
            if cnt == t:
                break
        
        if num == m:
            num = 0
        
        if len(s) > 0:
            s.pop(0)
    
    return answer

def getNum(i, n):
    
    result = ''
    while i > n-1:
        r = i%n
        if r > 9:
            start = ord('A')-10
            r = chr(start+r)
        
        result += str(r)
        i = i//n
    
    if i > 9:
        start = ord('A')-10
        i = chr(start+i)
        
    result += str(i)
    l = list(result)
    l.reverse()
    
    return ''.join(l)

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges