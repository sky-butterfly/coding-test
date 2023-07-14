from collections import deque

def solution(storey):
    answer = 0
    s = str(storey)
    size = len(s)
    
    queue = deque()
    queue.append((s, 0, 0))
    
    while queue:
        
        s, i, cnt = queue.popleft()
        size = len(s)
        
        if int(s) == 0 or ((size-i-1) < 0 or (size-i-1) >= size) :
            if int(s) == 0 and (answer == 0 or answer > cnt):
                answer = cnt
            continue
        
        ss = int(s[size-i-1])
        if ss == 0:
            queue.append((s, i+1, cnt))
            continue
        
        if answer == 0 or cnt+ss < answer: 
            queue.append((str(int(s) - ((10**i) * ss)), i+1, cnt+ss))
        
        s = str(int(s) + ((10**i) * (10-ss)))
        if answer == 0 or cnt+(10-ss) < answer:
            if size < len(s):
                queue.append((s, i+1, cnt+(10-ss)))
            else:
                queue.append((s, i+1, cnt+(10-ss)))
            
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges