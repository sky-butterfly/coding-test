def solution(w,h):
    answer = w * h
    
    mx = get(w, h)
    
    return answer - (w + h - mx)

def get(x, y):
    
    mn = min(x, y)
    
    i = mn
    while i > 0:
        if x%i == 0 and y%i == 0:
            break
            
        i -= 1
        
    return i
            
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges