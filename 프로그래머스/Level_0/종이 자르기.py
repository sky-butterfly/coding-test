def solution(M, N):
    answer = 0
    
    if N > M:
        answer = (M-1) + ( (N-1) * M )
    else:
        answer = (N-1) + ( (M-1) * N )
    
    return answer