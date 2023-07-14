from collections import deque

def solution(N, road, K):
    answer = 1
    answer_arr = [1]
    road.sort()
    
    obj = {1:0}
    queue = deque()
    queue.append(1)
    
    while queue:
        
        start = queue.popleft()
        time = obj[start]
        end = 0
        
        for r in road:
            
            a = r[0]
            b = r[1]
            c = r[2]
            
            if a != start and b != start :
                continue
                
            if a == start:
                end = b
            else:
                end = a
                
            end_time = time + c
            if end_time < obj.get(end, K+1):
                obj[end] = end_time
            
                if end_time <= K:
                    queue.append(end)
            
                    if end not in answer_arr:
                        answer_arr.append(end)
                        answer += 1
            
    return answer