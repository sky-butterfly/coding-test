from collections import deque

def solution(book_time):
    answer = 0
    book_time.sort()
    queue = []
    
    for bk in book_time:
        
        start = bk[0].split(':')
        s_h = int(start[0])
        s_m = int(start[1]) + (s_h * 60)
        
        end = bk[1].split(':')
        e_h = int(end[0])
        e_m = int(end[1]) + 10 + (e_h * 60)
        
        if len(queue) < 1 or (queue and queue[-1] < s_m):
            queue.append(e_m)
        else:
            while queue:

                q = queue[0]

                if q > s_m:
                    break

                queue.pop(0)

            queue.append(e_m)
        
        if len(queue) > answer:
            answer += 1
        
        queue.sort()
    
    return answer