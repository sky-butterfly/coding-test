def solution(want, number, discount):
    answer = 0
    total = 10
    obj = {}
    
    for i, w in enumerate(want):
        obj[w] = number[i]
    
    for i in range(len(discount)-9):
        d = discount[i:i+10]
        complete = True
        for i, w in enumerate(want):
            if (w in d) == False:
                complete = False
                break
            
            if number[i] != d.count(w):
                complete = False
                break
        if complete:
            answer += 1
    
    return answer