from collections import deque

def solution(m, n, board):
    answer = 0
    B = 'board'
    R = 'result'
    
    while board:
        obj = delete(m, n, board, B, R)
        board = obj[B]
        answer += obj[R]
    
    return answer

def delete(m, n, board, B, R):
    obj = {R : 0, B : board}
    
    n_arr = [0, 1, 1]
    m_arr = [1, 0, 1]
    delete = []
    
    for i, b in enumerate(board):
        for j, bb in enumerate(b):
            
            if bb == 0:
                continue
            
            check = True
            check_arr = [[i, j]]
            for k in range(3):
                x = i+m_arr[k]
                y = j+n_arr[k]
                if x < 0 or y < 0 or x >= m or y >= n:
                    check = False
                    break
                if bb != board[x][y]:
                    check = False
                    break
                check_arr.append([x,y])
            
            if check:
                delete.extend(check_arr)
    
    delete_set = []
    for d in delete:
        if (d in delete_set) == False:
            delete_set.append(d)
    
    if len(delete) == 0:
        obj[B] = []
        obj[R] = 0
        return obj
    
    o = {}
    for i in range(m):
        for j in range(n):
            if [i, j] in delete_set:
                continue
            
            if j in o.keys():
                temp = o[j]
                temp.append(board[i][j])
                o[j] = temp
            else:
                o[j] = [board[i][j]]
        
    for k in o.keys():
        for r in range(m-len(o[k])):
            temp = o[k]
            temp.insert(0, 0)
            o[k] = temp
    
    new_board = [[0]*n for i in range(m)]
    
    for i in range(m):
        for j in range(n): 
            if j in o.keys():
                new_board[i][j] = o[j][i]
            
    obj[B] = new_board
    obj[R] = len(delete_set)
    
    return obj