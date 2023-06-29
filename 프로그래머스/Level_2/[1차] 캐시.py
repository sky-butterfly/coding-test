from collections import deque

def solution(cacheSize, cities):
    answer = 0
    d = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for c in cities:
        cc = c.lower()
        
        if cc in d:
            answer += 1
            if d[len(d)-1] != cc:
                d.remove(cc)
                d.append(cc)
            continue
        
        answer += 5
        if len(d) >= cacheSize:
            d.popleft()
        d.append(cc)
    
    return answer