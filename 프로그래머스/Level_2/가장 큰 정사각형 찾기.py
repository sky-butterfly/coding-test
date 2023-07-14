def solution(board):
    
    x = [-1, 0, -1]
    y = [-1, -1, 0]
    
    for i, b in enumerate(board):
        for j, bb in enumerate(b):
            
            if board[i][j] == 0 or i == 0 or j == 0:
                continue
            
            a = board[i+x[0]][j+y[0]]
            b = board[i+x[1]][j+y[1]]
            c = board[i+x[2]][j+y[2]]
            
            mn = min(a, b, c)
            board[i][j] = mn+1
            
    mx = 0
    for b in board:
        for bb in b:
            if mx < bb:
                mx = bb
        
    return mx * mx

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges