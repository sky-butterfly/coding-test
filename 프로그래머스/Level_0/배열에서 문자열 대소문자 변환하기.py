def solution(strArr):
    answer = []
    
    for i, v in enumerate(strArr) :
        
        if i%2 == 0 :
            answer.append(v.lower())
            continue
        answer.append(v.upper())
    
    return answer