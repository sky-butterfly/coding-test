from collections import deque

def solution(x, y, n):
    answer = -1
    
    queue = deque()
    queue.append((y, 0))
    
    if x == y:
        return 0
    
    while queue:
        a, cnt = queue.popleft()
        
        cnt += 1
        
        if a%3 == 0:
            b = a // 3
            if b == x:
                answer = cnt
                break
            elif b > x:
                queue.append((b, cnt))
        
        if a%2 == 0:
            b = a // 2
            if b == x:
                answer = cnt
                break
            elif b > x:
                queue.append((b, cnt))
        
        b = a - n
        if b == x:
            answer = cnt
            break
        elif b > x:
            queue.append((b, cnt))
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges