def solution(board, k):
    answer = 0
    
    for i, b in enumerate(board):
        for j, bb in enumerate(b):
            if i+j <= k:
                answer += bb
    
    return answer