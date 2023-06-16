def solution(A, B):
    answer = 0
    
    if A == B :
        return answer
    
    for i in range(len(A)):
        
        if ( A[0] in B ) == False:
            answer = -1
            break
            
        A = A[len(A)-1] + A[0:len(A)-1]
        answer += 1
        
        if A == B:
            break
        
    if answer == len(A):
        answer = -1
    
    return answer