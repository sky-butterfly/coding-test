from collections import deque

def solution(maps):
    answer = []
    
    add_x = [-1, 1, 0, 0]
    add_y = [0, 0, -1, 1]
    size_x = len(maps)
    size_y = len(maps[0])
    
    visit = []
    
    for m in maps:
        visit.append([0]*len(m))
    
    for i, m in enumerate(maps):
        for j, mm in enumerate(m):
            
            if visit[i][j] == 1 or maps[i][j] == 'X':
                continue
            
            queue = deque()
            queue.append((i, j))
            num = 0
            while queue:
                
                q = queue.popleft()
                x, y = q

                if visit[x][y] == 1 or maps[x][y] == 'X':
                    continue
                
                num += int(maps[x][y])
                visit[x][y] = 1
                for k in range(4):

                    ax = x + add_x[k]
                    ay = y + add_y[k]

                    if ax < size_x and ay < size_y and ax >= 0 and ay >= 0:
                        queue.append((ax, ay))
            
            if num > 0:
                answer.append(num)
                
    if len(answer) < 1:
        answer = [-1]
        
    answer.sort()
    
    return answer