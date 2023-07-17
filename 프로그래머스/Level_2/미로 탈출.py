from collections import deque

def solution(maps):
    answer = -1
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    x_size = len(maps)
    y_size = len(maps[0])
    start_x = 0
    start_y = 0
    
    check = []
    for i, m in enumerate(maps):
        check.append([0]*y_size)
        
        if 'S' in m:
            start_x = i
            start_y = m.index('S')
    check[start_x][start_y] = 1
    
    queue = deque()
    queue.append((start_x, start_y, 0))
    while queue:
        
        x, y, time = queue.popleft()
        
        if maps[x][y] == 'L':
            answer = time
            start_x = x
            start_y = y
            break
        
        for i in range(4):
            xx = x+nx[i]
            yy = y+ny[i]
            if xx < 0 or xx >= x_size or yy < 0 or yy >= y_size:
                continue
            
            m = maps[xx][yy]
            if m == 'X' or check[xx][yy] == 1:
                continue
                
            queue.append((xx, yy, time+1))
            check[xx][yy] = 1
    
    if answer == -1:
        return answer
    
    check = []
    for i, m in enumerate(maps):
        check.append([0]*y_size)
    check[start_x][start_y] = 1
    
    answer2 = -1
    queue = deque()
    queue.append((start_x, start_y, 0))
    while queue:
        
        x, y, time = queue.popleft()
        
        if maps[x][y] == 'E':
            answer2 = time
            break
            
        for i in range(4):
            
            xx = x+nx[i]
            yy = y+ny[i]
            
            if xx < 0 or xx >= x_size or yy < 0 or yy >= y_size:
                continue
                
            m = maps[xx][yy]
            if m == 'X' or check[xx][yy] == 1:
                continue
                
            queue.append((xx, yy, time+1))
            check[xx][yy] = 1
    
    if answer2 == -1:
        answer = -1
    else:
        answer += answer2
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges