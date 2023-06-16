def solution(spell, dic):
    answer = 2
    
    for d in dic:
        
        flag = True
        
        for s in spell:
            if ( len(d) - len(d.replace(s, '')) )  != 1:
                flag = False
                break
        
        if flag :
            answer = 1
            break
    
    return answer