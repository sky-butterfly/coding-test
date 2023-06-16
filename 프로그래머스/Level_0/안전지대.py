def solution(board):
    answer = 0
    size = len(board)
    
    for b in range(size):
        for bb in range(size) :
            
            if board[b][bb] == 1:
                continue
            
            if bb+1 < size:
                if board[b][bb+1] == 1:
                    continue
            if bb-1 > -1:
                if board[b][bb-1] == 1:
                    continue
            if b-1 > -1:
                if bb+1 < size:
                    if board[b-1][bb+1] == 1:
                        continue
                if board[b-1][bb] == 1:
                    continue
                if bb-1 > -1:
                    if board[b-1][bb-1] == 1:
                        continue
                
            if b+1 < size:
                if bb+1 < size:
                    if board[b+1][bb+1] == 1:
                        continue
                if board[b+1][bb] == 1:
                    continue
                if bb-1 > -1:
                    if board[b+1][bb-1] == 1:
                        continue
            
            answer += 1        
                        
    return answer