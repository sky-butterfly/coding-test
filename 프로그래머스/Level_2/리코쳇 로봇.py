from collections import deque

def solution(board):
    answer = -1
    size_x = len(board)
    size_y = len(board[0])
    start_x = -1
    start_y = -1
    DIRECTION = 'top'
    
    check = []
    for i, b in enumerate(board):
        ch = []
        for j, bb in enumerate(b):
            if bb == 'R':
                start_x = i
                start_y = j
            ch.append({'top':0, 'bottom':0, 'right':0, 'left':0})
        check.append(ch)
    
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((start_x, start_y, 0))
    
    while queue:
        x, y, count = queue.popleft()
        
        if board[x][y] == 'G':
            answer = count
            break
            
        count += 1
        
        for i in range(4):
            xx = x + nx[i]
            yy = y + ny[i]
            
            direction = 'top'
            if i == 1:
                direction = 'bottom'
            elif i == 2:
                direction = 'left'
            elif i == 3:
                direction = 'right'
            
            block_count = 0
            while xx > -1 and xx < size_x and yy > -1 and yy < size_y:
                    
                c_obj = check[xx][yy]                
                c = c_obj[direction]
                if c == 1 or board[xx][yy] == 'D':
                    break
                    
                check[xx][yy][direction] = 1
                
                if direction == 'top':
                    xx -= 1
                elif direction == 'bottom':
                    xx += 1
                elif direction == 'left':
                    yy -= 1
                else:
                    yy += 1
                
                block_count += 1
            
            if block_count > 0:
                if direction == 'top':
                    xx = x + (nx[i] * block_count)
                elif direction == 'bottom':
                    xx = x + (nx[i] * block_count)
                elif direction == 'left':
                    yy = y + (ny[i] * block_count)
                else:
                    yy = y + (ny[i] * block_count)
            
                queue.append((xx, yy, count))
            
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges