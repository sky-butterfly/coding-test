def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        x = a + (i*d)
        
        if included[i] == True :
            answer += x
            
    return answer
