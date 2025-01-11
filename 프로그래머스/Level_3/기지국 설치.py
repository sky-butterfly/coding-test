def solution(n, stations, w):
    answer = 0

    arr = []
    
    start = 1
    mx = 1
    
    for s in stations:
        
        mn = s - w
        mx = s + w
        
        if start < mn :            
            arr.append((start, mn))
            
        start = mx + 1
        
    if start <= n:
        arr.append((start, n + 1))
        
    for a in arr:
        
        num = a[1] - a[0]
        need = num // ( w * 2 + 1 )
        add = num % ( w * 2 + 1 )
        
        if add > 0:
            add = 1
        
        answer += (need + add)
        

    return answer


# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges