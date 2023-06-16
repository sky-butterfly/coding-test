def solution(keyinput, board):
    answer = [0,0]    
    
    h_limit = int(board[1]/2)
    w_limit = int(board[0]/2)
    
    for k in keyinput:
        if k == 'left':
            i = answer[0]
            if abs(i-1) <= w_limit:
                answer[0] = i-1
        if k == 'right':
            i = answer[0]
            if abs(i+1) <= w_limit:
                answer[0] = i+1
        if k == 'up':
            i = answer[1]
            if abs(i+1) <= h_limit:
                answer[1] = i+1
        if k == 'down':
            i = answer[1]
            if abs(i-1) <= h_limit:
                answer[1] = i-1
            
    return answer