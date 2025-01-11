def solution(routes):
    answer = 1
    
    arr = []
    
    mi = -30000
    mx = 30000
    
    routes = sorted(routes) 
    
    for r in routes:
        
        first = r[0]
        second = r[1]
        
        if second < first :
            first = r[1]
            second = r[0]
        
        if first > mi :
            mi = first
            
        if mi > mx :
            answer += 1
            mx = second
            
            continue
            
        if second < mx :
            mx = second
        
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges