def solution(names):
    answer = []
    size = int(len(names)/5)
    
    answer.append(names[0])
    for s in range(1, size) :
        answer.append(names[5*s])
        
    if len(names)%5 > 0 :
        answer.append(names[5*size])
    
    return answer