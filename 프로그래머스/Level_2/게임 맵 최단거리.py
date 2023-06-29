from collections import deque

def solution(maps):
    answer = 0
    
    x_size = len(maps)
    y_size = len(maps[0])
    
    x_arr = [0, 0, -1, 1]
    y_arr = [1,-1, 0, 0]
    
    queue = deque()
    queue.append([0,0])
    while len(queue) > 0:
        l = queue.popleft()
        x = l[0]
        y = l[1]
        for i in range(4):
            nx = x + x_arr[i]
            ny = y + y_arr[i]
            if (nx >= 0 and nx < x_size) and (ny >= 0 and ny < y_size) and (maps[nx][ny] == 1):
                maps[nx][ny] = maps[x][y]+1
                queue.append([nx,ny])   
                
    result = maps[x_size-1][y_size-1]
    
    if result == 1:
        return -1
    
    return result