from collections import deque
import heapq

def solution(n, k, enemy):
    answer = 0 
    if k >= len(enemy):
        return len(enemy)
    
    l = enemy.copy()
    l.sort(reverse=True)
    
    l, ll = l[:k], l[k:]
    if sum(ll) <= n:
        return len(enemy)
    
    arr = []
    total = 0
    for e in enemy:
        total += e
        heapq.heappush(arr, e)
        
        if k > 0:
            k -= 1
            answer += 1
            continue
        
        h = heapq.heappop(arr)
        if n < h:
            break
        
        n -= h
        answer += 1
        
        
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges