from collections import deque

def solution(order):
    answer = 0
    
    stack = deque()
    queue = deque()
    order_q = deque(order)
    
    for i in range(1, len(order)+1):
        queue.append(i)
        
    while order_q:
        finish = False
        
        oq = order_q.popleft()
        
        if stack and oq == stack[-1]:
            answer += 1
            stack.pop()
            continue
        
        while queue:
            q = queue.popleft()
            
            if oq == q:
                answer += 1
                break
            if oq > q:
                stack.append(q)
                continue
            
            if stack and oq == stack[-1]:
                stack.pop()
                answer += 1
                break
            
            finish = True
            break
    
        if finish:
            break
                
    
    return answer