from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    obj = {}
    
    n = 0
    limit = (len(q1) + len(q2)) * 2
    while len(q1) > 0 and len(q2) > 0:
        
        if n > limit:
            answer = -1
            break
            
        if sum_q1 == sum_q2:
            answer = n
            break
        
        if sum_q2 > sum_q1:
            num = q2.popleft()
            sum_q2 -= num
            q1.append(num)
            sum_q1 += num
        else:
            num = q1.popleft()
            sum_q1 -= num
            q2.append(num)
            sum_q2 += num
        
        n += 1
    
        if len(q1) == 0 or len(q2) == 0:
            answer = -1
            break
    
    return answer